#!/usr/bin/env python3
"""
ask.py — Ask questions against your embedded study guide.

Loads the vector store built by ingest.py, embeds your question, finds
the most relevant chunks by cosine similarity, and asks a local Ollama
chat model to answer using only that retrieved context (classic RAG).

Usage:
    python ask.py --store store.json
    (then just type questions at the prompt)
"""

import argparse
import json
import math
import sys
from pathlib import Path

import requests

OLLAMA_HOST = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "llama3.2"
TOP_K = 4  # how many chunks to retrieve per question

SYSTEM_PROMPT = """You are a study assistant helping someone prepare for \
the AWS Certified Cloud Practitioner (CLF-C02) exam. Answer the question \
using ONLY the provided context from their study guide. If the context \
doesn't contain enough information to answer confidently, say so clearly \
rather than guessing. Keep answers focused and exam-relevant. When useful, \
mention which domain/topic the answer relates to."""


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def embed_text(text: str, model: str, host: str):
    resp = requests.post(
        f"{host}/api/embeddings",
        json={"model": model, "prompt": text},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["embedding"]


def retrieve(question: str, store: list, model: str, host: str, top_k: int):
    q_vector = embed_text(question, model, host)
    scored = [
        (cosine_similarity(q_vector, chunk["embedding"]), chunk)
        for chunk in store
    ]
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:top_k]


def build_context(scored_chunks):
    parts = []
    for score, chunk in scored_chunks:
        header = f"[{chunk['domain']} — {chunk['section']}]"
        parts.append(f"{header}\n{chunk['text']}")
    return "\n\n---\n\n".join(parts)


def ask_llm(question: str, context: str, model: str, host: str):
    prompt = f"""{SYSTEM_PROMPT}

Context from study guide:
---
{context}
---

Question: {question}

Answer:"""
    resp = requests.post(
        f"{host}/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "options": {"temperature": 0.2},
        },
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()["response"].strip()


def main():
    parser = argparse.ArgumentParser(description="Ask questions against your study guide")
    parser.add_argument("--store", default=Path("store.json"), type=Path,
                         help="Path to the vector store built by ingest.py")
    parser.add_argument("--embed-model", default=EMBED_MODEL,
                         help=f"Ollama embedding model (default: {EMBED_MODEL})")
    parser.add_argument("--chat-model", default=CHAT_MODEL,
                         help=f"Ollama chat model (default: {CHAT_MODEL})")
    parser.add_argument("--host", default=OLLAMA_HOST,
                         help=f"Ollama host URL (default: {OLLAMA_HOST})")
    parser.add_argument("--top-k", default=TOP_K, type=int,
                         help=f"Number of chunks to retrieve (default: {TOP_K})")
    parser.add_argument("--show-sources", action="store_true",
                         help="Print which sections were retrieved for each answer")
    args = parser.parse_args()

    if not args.store.exists():
        print(f"Store not found: {args.store}. Run ingest.py first.", file=sys.stderr)
        sys.exit(1)

    store = json.loads(args.store.read_text())
    print(f"[*] Loaded {len(store)} chunks from {args.store}")
    print("[*] Type your question and press enter. Type 'quit' or 'exit' to stop.\n")

    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if not question:
            continue
        if question.lower() in ("quit", "exit", "/bye"):
            print("Bye!")
            break

        try:
            scored_chunks = retrieve(question, store, args.embed_model, args.host, args.top_k)
        except requests.RequestException as exc:
            print(f"[!] Retrieval failed (is Ollama running?): {exc}\n")
            continue

        if args.show_sources:
            print("[sources]", ", ".join(
                f"{c['section'] or c['domain']} ({s:.2f})" for s, c in scored_chunks
            ))

        context = build_context(scored_chunks)
        try:
            answer = ask_llm(question, context, args.chat_model, args.host)
        except requests.RequestException as exc:
            print(f"[!] Generation failed: {exc}\n")
            continue

        print(f"\nBuddy: {answer}\n")


if __name__ == "__main__":
    main()
