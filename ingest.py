#!/usr/bin/env python3
"""
ingest.py — Chunk study material and build a local vector store.

Splits a markdown study guide into section-sized chunks (using ## headers
as natural boundaries, tagged with their parent # domain), embeds each
chunk with a local Ollama embedding model, and saves everything to a
JSON file that ask.py can search against.

Usage:
    python ingest.py --input aws-clf-c02-study-guide.md --out store.json
"""

import argparse
import json
import sys
from pathlib import Path

import requests

OLLAMA_HOST = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"

# Keep chunks from getting too large for good retrieval — if a section
# under a ## header is longer than this many characters, split it further
# on paragraph breaks.
MAX_CHUNK_CHARS = 2500


def chunk_markdown(text: str):
    """Split markdown into chunks along # and ## headers.

    Each chunk keeps track of its domain (# header) and section title
    (## header) as metadata, which we'll show alongside answers so you
    can see exactly which part of your notes an answer came from.
    """
    lines = text.split("\n")
    chunks = []
    current_domain = ""
    current_section = ""
    current_lines = []

    def flush():
        content = "\n".join(current_lines).strip()
        if content:
            chunks.append({
                "domain": current_domain,
                "section": current_section,
                "text": content,
            })

    for line in lines:
        if line.startswith("# ") and not line.startswith("## "):
            flush()
            current_lines = []
            current_domain = line.lstrip("# ").strip()
            current_section = ""
        elif line.startswith("## "):
            flush()
            current_lines = []
            current_section = line.lstrip("# ").strip()
        else:
            current_lines.append(line)
    flush()

    # Further split any oversized chunks on blank-line paragraph breaks,
    # so no single chunk overwhelms the model's context or dilutes
    # retrieval relevance.
    final_chunks = []
    for c in chunks:
        if len(c["text"]) <= MAX_CHUNK_CHARS:
            final_chunks.append(c)
            continue
        parts = c["text"].split("\n\n")
        buf = ""
        for part in parts:
            if len(buf) + len(part) > MAX_CHUNK_CHARS and buf:
                final_chunks.append({**c, "text": buf.strip()})
                buf = ""
            buf += part + "\n\n"
        if buf.strip():
            final_chunks.append({**c, "text": buf.strip()})

    return final_chunks


def embed_text(text: str, model: str, host: str):
    resp = requests.post(
        f"{host}/api/embeddings",
        json={"model": model, "prompt": text},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["embedding"]


def main():
    parser = argparse.ArgumentParser(description="Chunk and embed a study guide")
    parser.add_argument("--input", required=True, type=Path,
                         help="Path to the markdown study guide")
    parser.add_argument("--out", default=Path("store.json"), type=Path,
                         help="Output path for the vector store (default: store.json)")
    parser.add_argument("--model", default=EMBED_MODEL,
                         help=f"Ollama embedding model (default: {EMBED_MODEL})")
    parser.add_argument("--host", default=OLLAMA_HOST,
                         help=f"Ollama host URL (default: {OLLAMA_HOST})")
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    text = args.input.read_text(encoding="utf-8")
    chunks = chunk_markdown(text)
    print(f"[*] Split into {len(chunks)} chunks")

    store = []
    for i, chunk in enumerate(chunks, 1):
        label = chunk["section"] or chunk["domain"] or f"chunk {i}"
        print(f"[{i}/{len(chunks)}] Embedding: {label[:60]}")
        try:
            vector = embed_text(chunk["text"], args.model, args.host)
        except requests.RequestException as exc:
            print(f"  [!] Failed to embed chunk {i}: {exc}", file=sys.stderr)
            print("  [!] Is Ollama running? (ollama serve)", file=sys.stderr)
            sys.exit(1)
        store.append({
            "id": i,
            "domain": chunk["domain"],
            "section": chunk["section"],
            "text": chunk["text"],
            "embedding": vector,
        })

    args.out.write_text(json.dumps(store))
    print(f"\n[*] Saved {len(store)} embedded chunks to {args.out}")


if __name__ == "__main__":
    main()
