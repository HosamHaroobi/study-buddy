# AWS Certified Cloud Practitioner (CLF-C02) — Comprehensive Study Guide

> Purpose: deep, exam-level reference material organized by the official exam guide domains and task statements. Written for both human study and downstream AI training use.

## Exam Domain Weighting

| Domain | Weight |
|---|---|
| 1. Cloud Concepts | 24% |
| 2. Security and Compliance | 30% |
| 3. Cloud Technology and Services | 34% |
| 4. Billing, Pricing, and Support | 12% |

---

# DOMAIN 1: Cloud Concepts (24%)

## Task Statement 1.1 — Benefits of the AWS Cloud

**Core value proposition:** AWS lets customers trade capital expense (CapEx) for variable expense (OpEx), benefit from massive economies of scale, stop guessing at capacity, increase speed and agility, stop spending money running and maintaining data centers, and go global in minutes.

**Six advantages of cloud computing (classic AWS framing):**
1. Trade capital expense for variable expense — pay only for compute/storage you consume instead of investing heavily in data centers before you know your usage.
2. Benefit from massive economies of scale — aggregated usage from hundreds of thousands of customers gives AWS higher economies of scale, which translates into lower pay-as-you-go prices.
3. Stop guessing capacity — no more over-provisioning "just in case" or under-provisioning and running into shortages; scale up or down as needed with minutes of notice.
4. Increase speed and agility — new IT resources are a click away, reducing the time to make resources available to developers from weeks to minutes.
5. Stop spending money running and maintaining data centers — focus on projects that differentiate the business, not on the "undifferentiated heavy lifting" of racking, stacking, and powering servers.
6. Go global in minutes — deploy applications in multiple AWS Regions around the world with a few clicks, providing lower latency and a better experience for customers at minimal cost.

**Global infrastructure benefits (speed of deployment, global reach):**
- Because AWS infrastructure already exists worldwide, a customer can deploy a workload to a new geographic market in minutes rather than the months/years it would take to build a physical data center there.
- Global reach lets a company serve customers with low latency in many parts of the world without owning any physical infrastructure in those locations.
- This global footprint also supports disaster recovery and business continuity by allowing workloads to be replicated to a separate geographic area.

**High availability, elasticity, and agility:**
- **High availability (HA):** the ability of a system to remain operational and accessible with minimal downtime, typically achieved by removing single points of failure — e.g., running resources across multiple Availability Zones so the failure of one AZ doesn't take down the application.
- **Elasticity:** the ability to automatically or easily scale resources (up or down, in or out) to match demand — you pay for what you need at any given time rather than provisioning for peak load year-round. Auto Scaling is the primary mechanism for elasticity on AWS.
- **Agility:** the ability to rapidly develop, test, and launch software applications, because IT resources are available on-demand — this shortens the time between an idea and a deployed solution, enabling experimentation with low financial risk (if an experiment fails, you simply decommission the resources without having sunk capital into them).

**Exam angle / common gotchas:**
- Don't confuse *elasticity* (automatic/rapid resource scaling to match demand) with *scalability* (the general capability of a system to handle growth — elasticity is a specific, often automated, form of scalability).
- "Economies of scale" refers to AWS's cost advantage from aggregating demand across all customers — not an individual customer's own volume discount (though volume discounts on some services are a separate, related benefit).
- Global infrastructure questions often test *why* you'd deploy to a new Region: lower latency for end users in that geography, data sovereignty/legal requirements, or disaster recovery — not simply "because it's available."

## Task Statement 1.2 — AWS Well-Architected Framework

The **AWS Well-Architected Framework** provides a consistent, structured approach for evaluating architectures and implementing designs that scale over time. It is organized into **six pillars**:

1. **Operational Excellence** — the ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures. Key ideas: perform operations as code (IaC), make frequent small reversible changes, refine operations procedures frequently, anticipate failure, and learn from all operational failures.
2. **Security** — the ability to protect data, systems, and assets to take advantage of cloud technologies to improve security. Key ideas: implement a strong identity foundation, enable traceability (logging/monitoring), apply security at all layers (defense in depth), automate security best practices, protect data in transit and at rest, keep people away from data (minimize direct/manual access), and prepare for security events (incident response).
3. **Reliability** — the ability of a system to recover from infrastructure or service disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions such as misconfigurations or transient network issues. Key ideas: automatically recover from failure, test recovery procedures, scale horizontally to increase aggregate system availability, stop guessing capacity, and manage change through automation.
4. **Performance Efficiency** — the ability to use computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve. Key ideas: democratize advanced technologies (consume managed services rather than build expertise from scratch), go global in minutes, use serverless architectures, experiment more often, and consider mechanical sympathy (choose the right resource/service type for the job, e.g., matching instance/storage types to workload characteristics).
5. **Cost Optimization** — the ability to run systems to deliver business value at the lowest price point. Key ideas: implement cloud financial management, adopt a consumption model (pay only for what you use), measure overall efficiency, stop spending money on undifferentiated heavy lifting (use managed services), and analyze and attribute expenditure (cost allocation tags, showback/chargeback).
6. **Sustainability** — the ability to minimize the environmental impacts of running cloud workloads. Key ideas: understand your impact and measure it, set sustainability goals, maximize utilization, anticipate and adopt new, more efficient hardware and software offerings, use managed services (AWS optimizes the shared infrastructure), and reduce the downstream impact of your cloud usage (e.g., reducing customer device/network energy use).

**How the pillars differ from one another (a common exam distinction):**
- Security vs. Reliability: security is about protecting against *intentional* threats and unauthorized access; reliability is about recovering from *unintentional* disruptions (hardware failure, network blips, misconfiguration) and meeting availability/recovery targets.
- Cost Optimization vs. Performance Efficiency: cost optimization is about spending efficiently for the value delivered; performance efficiency is about using the *right* resources efficiently — these can align, but performance efficiency is not simply "the cheapest option."
- Sustainability is the newest pillar (added 2021) and is distinct in focusing on environmental impact rather than purely business/technical outcomes.

**Exam angle / gotchas:**
- Expect scenario questions naming a business need (e.g., "the company wants to reduce its carbon footprint," "the company wants systems to recover automatically from an AZ failure," "the company wants to track and reduce unnecessary spend") and asking which pillar it maps to.
- The Well-Architected Framework is implemented in practice via the **AWS Well-Architected Tool**, a free service in the console that lets you review workloads against the pillars and get improvement recommendations (this tool itself is more of a Domain 3 fact, but the two are often linked in questions).

## Task Statement 1.3 — Cloud Migration Benefits and Strategies

**AWS Cloud Adoption Framework (AWS CAF)** provides guidance to help organizations develop an efficient and effective plan for their cloud adoption journey. It groups organizational capabilities into **six perspectives**:
1. **Business** — ensures IT aligns with business needs and that the business case/value of cloud investment is understood (roles: business managers, finance managers, budget owners, strategy stakeholders).
2. **People** — focuses on people development, training, and change management to bridge gaps in skills and organizational structures (HR, staffing, people managers).
3. **Governance** — focuses on the skills and processes to align IT strategy and goals with business strategy and goals, to maximize business value and minimize risks (CIO, program managers, enterprise architects, business analysts, portfolio managers).
4. **Platform** — helps describe, design, and implement new solutions on the cloud, including hybrid and legacy environments (CTO, architects, engineers).
5. **Security** — ensures the organization meets its security objectives for visibility, auditability, control, and agility (CISO, security architects/analysts).
6. **Operations** — focuses on how to enable, run, use, operate, and recover IT workloads to the level agreed upon with business stakeholders (IT operations managers, site reliability engineers).

**Business outcomes AWS CAF helps drive** (explicitly called out in the exam guide): reduced business risk, improved ESG (environmental, social, and governance) performance, increased revenue, and increased operational efficiency.

**Migration strategies — the "6 Rs" (originally "5 Rs," now commonly extended to 6 or 7):**
- **Rehost ("lift and shift"):** move applications as-is to AWS with no code changes; fastest, lowest initial effort; good first step for large migrations.
- **Replatform ("lift, tinker, and shift"):** make a few cloud optimizations without changing core architecture, e.g., moving a database to Amazon RDS instead of self-managing it on EC2.
- **Repurchase ("drop and shop"):** move to a different product, typically a SaaS platform, e.g., moving a CRM to Salesforce.
- **Refactor / Re-architect:** reimagine how the application is architected using cloud-native features, typically driven by a strong business need to add features, scale, or improve performance that's hard to achieve in the current environment.
- **Retire:** decommission or remove applications that are no longer needed once you determine they're not being used.
- **Retain:** keep applications that are not ready to migrate (e.g., recently upgraded, or requiring major refactoring not currently justified) — sometimes called "revisit."

**Migration/data-transfer tools relevant here:**
- **AWS Database Migration Service (AWS DMS):** migrates databases to AWS with minimal downtime; source database remains fully operational during migration; supports homogeneous (e.g., Oracle-to-Oracle) and heterogeneous (e.g., Oracle-to-Aurora) migrations.
- **AWS Schema Conversion Tool (AWS SCT):** used alongside DMS for heterogeneous migrations — it converts the source database schema and most database code objects (views, stored procedures, functions) to a format compatible with the target database.
- **AWS Application Discovery Service:** helps plan migration by collecting usage and configuration data about on-premises servers.
- **AWS Application Migration Service (MGN):** AWS's recommended lift-and-shift (rehost) service for migrating physical, virtual, and cloud servers to AWS.
- **AWS Migration Hub:** a central place to track the progress of application migrations across multiple AWS and partner tools.
- **Migration Evaluator:** helps build a data-driven business case for migrating to AWS by analyzing on-premises environments.

**Exam angle / gotchas:**
- Given a scenario describing an action (e.g., "moving an app to a SaaS CRM," "moving a VM as-is with no changes," "decommissioning an unused legacy app"), identify the correct "R."
- AWS CAF perspectives questions typically give you a *role* (e.g., CISO, business analyst, HR manager) or a *goal* and ask which perspective it belongs to.
- Know that DMS keeps the source DB operational during migration (minimizing downtime) — a frequently tested fact.

## Task Statement 1.4 — Cloud Economics

**Fixed costs vs. variable costs:**
- **Fixed costs:** costs that do not change regardless of usage — classic on-premises examples include the upfront capital investment in physical servers, real estate/data center facilities, and the depreciation of hardware over time, regardless of how much it is actually used.
- **Variable costs (AWS pay-as-you-go model):** costs scale with actual consumption — you pay only for the compute, storage, and network resources you actually use, and costs go up or down as usage changes.
- The cloud converts CapEx to OpEx: instead of large upfront investments (CapEx) in infrastructure that may or may not be fully utilized, you have ongoing, usage-based operational expenses (OpEx).

**Costs associated with on-premises environments (beyond just hardware):**
- Real estate / facility costs (power, cooling, physical security, floor space).
- Hardware procurement, and the risk of over- or under-provisioning capacity.
- IT labor for racking, stacking, patching, and maintaining physical infrastructure.
- Redundant infrastructure required for high availability and disaster recovery, which often sits idle most of the time.
- Depreciation and eventual hardware refresh/replacement cycles.
- Opportunity cost — capital tied up in infrastructure instead of the core business.

**Licensing strategies:**
- **Bring Your Own License (BYOL):** you bring an existing software license (e.g., an Oracle or Microsoft SQL Server license you already own) and use it on AWS infrastructure, typically paying only for the underlying compute/infrastructure and not an additional bundled software fee.
- **License-included:** AWS bundles the cost of the third-party software license into the hourly or usage-based price of the service (e.g., certain RDS engine options), so you don't need to separately procure or manage a license.
- Choosing between them depends on whether you have existing, transferable licenses (favoring BYOL) versus wanting simplicity and avoiding license management overhead (favoring license-included).

**Rightsizing:** the practice of matching instance types and sizes (or service tiers) to actual workload performance and capacity requirements at the lowest possible cost — avoiding both over-provisioning (paying for unused capacity) and under-provisioning (risking performance problems). AWS Compute Optimizer and Cost Explorer's rightsizing recommendations are the tools most associated with this practice.

**Benefits of automation (cost angle):**
- Reduces human error and the operational labor cost of manual tasks (patching, deployments, scaling).
- Enables faster, more consistent, and repeatable processes (e.g., via Infrastructure as Code), which reduces the cost of managing environments at scale.
- Enables automatic scaling (elasticity) so you're not paying for idle capacity, and not manually intervening to scale up/down.

**Economies of scale:** because AWS aggregates usage from a massive number of customers, it can negotiate better rates on hardware, power, networking, etc., and pass a portion of those savings on to customers via continually decreasing prices over time — an individual company could not achieve the same purchasing power on its own.

**Exam angle / gotchas:**
- Watch for questions contrasting CapEx (on-prem, fixed, upfront) vs. OpEx (cloud, variable, pay-as-you-go) — this is one of the most frequently tested Domain 1 concepts.
- BYOL vs. license-included questions usually hinge on whether the company "already owns licenses" (→ BYOL) vs. wants a fully bundled, hands-off cost model (→ license-included).
- Rightsizing is about matching *capacity to need*, not simply "choosing the cheapest option" — don't confuse it with Spot Instances or Savings Plans (which are pricing/purchasing options, covered in Domain 4).

---

# DOMAIN 2: Security and Compliance (30%)

## Task Statement 2.1 — AWS Shared Responsibility Model

The **Shared Responsibility Model** divides security and compliance responsibilities between AWS and the customer.

**AWS is responsible for "Security OF the Cloud":**
- Protecting the global infrastructure that runs all AWS services: Regions, Availability Zones, and edge locations.
- The physical security of data centers (access control, video surveillance, staffing).
- The hardware, software, networking, and facilities that run AWS services.
- For managed services, AWS also handles the underlying operating system, patching, and platform management.

**Customers are responsible for "Security IN the Cloud":**
- Customer data — classification, encryption, and management of their own data.
- Identity and access management — configuring IAM users, groups, roles, and policies correctly.
- Operating system, network, and firewall configuration for resources they manage (e.g., patching an EC2 instance's guest OS).
- Client-side and server-side data encryption and network traffic protection.
- Platform, application, and identity management for anything running *on top of* AWS infrastructure.

**How responsibility shifts depending on the service model:**
- **Infrastructure as a Service (IaaS) — e.g., Amazon EC2:** AWS manages the physical hardware, networking, and virtualization layer; the customer is responsible for the guest OS (including updates and security patches), any application software installed, firewall configuration (security groups), and IAM/data security. This is the model where the customer has the *most* responsibility.
- **Platform as a Service (PaaS) — e.g., Amazon RDS:** AWS manages more of the stack, including the underlying OS and database engine software/patching; the customer remains responsible for their data, access management, and some configuration (e.g., which data is stored, network access rules, backup retention settings).
- **Software/Function as a Service — e.g., AWS Lambda, Amazon S3:** AWS manages nearly the entire underlying stack (including the runtime for Lambda); the customer is responsible mainly for their code/data, IAM permissions, and configuration choices (e.g., S3 bucket policies, encryption settings).
- General rule: the more "managed" the service, the more of the operational/security burden shifts to AWS — but the customer is *always* responsible for data, identity and access management, and correctly configuring the service.

**Exam angle / gotchas:**
- The single most tested idea in Domain 2: **"security OF the cloud" = AWS; "security IN the cloud" = customer.**
- Expect scenario questions asking "who is responsible for X" for a specific service (e.g., "Who patches the guest OS on an EC2 instance?" → customer; "Who patches the underlying host/hypervisor?" → AWS; "Who manages OS patching for RDS?" → AWS; "Who is responsible for configuring an S3 bucket policy correctly?" → customer).
- Data encryption is a *shared* responsibility in practice — AWS provides the tools and capability (e.g., KMS, S3 SSE), but the customer decides whether/how to enable and configure encryption.

## Task Statement 2.2 — AWS Cloud Security, Governance, and Compliance Concepts

**Where to find AWS compliance information:**
- **AWS Artifact:** a self-service portal in the console providing on-demand access to AWS's compliance reports (SOC reports, ISO certifications, PCI reports) and the ability to review and accept agreements such as the Business Associate Addendum (BAA) for HIPAA. This is the primary tested tool for "where do I get compliance documentation."

**Compliance needs vary by geography/industry:**
- Different Regions/countries have different legal and regulatory requirements (e.g., GDPR in the EU, data residency laws requiring data to stay within national borders).
- Different industries have specific compliance frameworks (e.g., HIPAA for healthcare, PCI DSS for payment card data, FedRAMP for U.S. federal government workloads).
- AWS achieves and maintains certifications against many of these frameworks so customers can build compliant workloads, but the *customer* is responsible for using the services in a way that satisfies the specific regulation applicable to them (an extension of the shared responsibility model into the compliance space).

**Services that help customers secure resources on AWS:**
- **Amazon Inspector:** automated vulnerability management service that continuously scans EC2 instances, container images (in Amazon ECR), and Lambda functions for software vulnerabilities and unintended network exposure.
- **AWS Security Hub:** a cloud security posture management service that aggregates, organizes, and prioritizes security findings/alerts from multiple AWS services (GuardDuty, Inspector, Macie, etc.) and third-party tools into a single dashboard, and runs automated checks against security standards (e.g., CIS AWS Foundations Benchmark).
- **Amazon GuardDuty:** an intelligent threat detection service that continuously monitors for malicious activity and unauthorized behavior by analyzing VPC Flow Logs, DNS logs, and CloudTrail management/data events, using machine learning and threat intelligence feeds.
- **AWS Shield:** managed Distributed Denial of Service (DDoS) protection. **Shield Standard** is automatically enabled for all AWS customers at no additional cost and protects against common, most-frequently-occurring network and transport layer DDoS attacks. **Shield Advanced** is a paid service offering more comprehensive protection, near-real-time visibility, and access to the AWS DDoS Response Team (DRT).

**Encryption options:**
- **Encryption at rest:** protects data while it is stored (e.g., on EBS volumes, in S3 buckets, in RDS databases) — typically implemented using AWS Key Management Service (KMS) keys.
- **Encryption in transit:** protects data as it moves across a network (e.g., between a client and AWS, or between AWS services) — typically implemented via TLS/SSL.
- Both are commonly managed with **AWS KMS** (Key Management Service), which lets you create and control encryption keys, and **AWS CloudHSM**, which provides dedicated hardware security modules for customers with strict compliance requirements needing single-tenant control over key material.

**Governance and compliance services (monitoring, auditing, reporting):**
- **Amazon CloudWatch — Monitoring:** collects and tracks metrics, collects and monitors log files, and sets alarms; used to observe resource/application performance and health in near real time.
- **AWS CloudTrail — Auditing:** records API calls and account activity across your AWS account (who did what, when, and from where) — essential for security analysis, operational troubleshooting, and compliance auditing. CloudTrail is *the* auditing/governance tool tested most often.
- **AWS Config — Auditing/Compliance:** records and evaluates the configurations of your AWS resources over time, allowing you to assess, audit, and evaluate configurations against desired baselines, and see configuration change history.
- **Reporting with access reports:** IAM provides access reports (e.g., IAM Access Analyzer findings, credential reports, service last-accessed data) to help review who/what has access to resources and identify unused permissions.

**Exam angle / gotchas:**
- CloudTrail vs. CloudWatch vs. Config is one of the most commonly confused trios: **CloudTrail = who did what (API activity log/audit trail)**; **CloudWatch = performance/operational monitoring, metrics, and alarms**; **Config = tracks resource configuration state/history and compliance against rules.**
- GuardDuty vs. Inspector vs. Security Hub: **GuardDuty = threat detection (is something malicious happening right now)**; **Inspector = vulnerability scanning (are my resources configured with known weaknesses)**; **Security Hub = aggregation/dashboard of findings from many sources.**
- AWS Artifact is for *downloading/reviewing compliance reports and agreements* — it does not scan your account or generate findings about your own resources.

## Task Statement 2.3 — AWS Access Management Capabilities

**AWS Identity and Access Management (IAM)** is the core service for controlling who can do what in an AWS account.
- **Users:** represent an individual person or application; have long-term credentials (password for console, access keys for programmatic access).
- **Groups:** collections of users, used to apply the same set of permissions to multiple users at once.
- **Roles:** an identity with permission policies that can be *assumed* temporarily by users, applications, or AWS services (e.g., an EC2 instance assuming a role to access S3) — roles use temporary security credentials rather than long-term ones, and are the recommended approach whenever possible.
- **Policies:** JSON documents that define permissions. **Managed policies** (AWS-managed or customer-managed) are standalone, reusable policies. **Custom (inline) policies** are embedded directly in a single user, group, or role.

**Principle of least privilege:** grant only the minimum permissions necessary for a user or role to perform its required task, and nothing more — reducing the blast radius if credentials are ever compromised. This is a core, frequently tested security concept.

**Root user protection:**
- The **root user** is created when the AWS account is first created and has complete, unrestricted access to all resources and billing information in the account.
- Best practice: do not use the root user for everyday tasks — create individual IAM users (or federated identities) with only the permissions they need, and lock away root credentials.
- **Tasks that only the root user can perform** (a specifically called-out exam skill) include things like: changing the account's support plan, closing the AWS account, changing the account name/email/root password, restoring IAM user permissions if the sole administrator locked themselves out, and some other account-level/billing settings.
- **Root user protection methods:** enable multi-factor authentication (MFA) on the root user, use a strong/unique password, avoid creating access keys for the root user (delete them if they exist), and use the root user only for the specific tasks that require it.

**Authentication methods:**
- **Multi-factor authentication (MFA):** requires a second authentication factor (e.g., a virtual MFA device/authenticator app, hardware security key, or SMS in some contexts) in addition to a password — should be enabled for the root user and ideally all IAM users, especially privileged ones.
- **AWS IAM Identity Center** (formerly AWS Single Sign-On/SSO): provides centralized access management for multiple AWS accounts and business applications; lets users sign in once with a single set of credentials to access all their assigned accounts/apps — the recommended way to manage human user access at scale, especially with AWS Organizations.
- **Cross-account IAM roles:** allow a user or service in one AWS account to assume a role and gain temporary access to resources in a *different* AWS account, without needing to create a separate IAM user in each account — a key mechanism for secure multi-account access (common in AWS Organizations setups).
- **Federated identity:** allows users to authenticate using an external identity provider (e.g., corporate Active Directory, or a social identity provider via Amazon Cognito) instead of creating a distinct IAM user — the identity is "federated" into AWS, typically resulting in a temporary role session rather than a standing IAM user.

**Access keys, password policies, and credential storage:**
- **Access keys** (access key ID + secret access key) provide programmatic (CLI/SDK/API) access; should be rotated regularly and never hard-coded or committed to source control.
- **IAM password policies** let administrators enforce rules on console passwords: minimum length, character complexity requirements, expiration/rotation periods, password reuse prevention.
- **AWS Secrets Manager:** securely stores, manages, and automatically rotates secrets such as database credentials, API keys, and other sensitive strings that applications need at runtime.
- **AWS Systems Manager (Parameter Store, part of Systems Manager):** provides secure, hierarchical storage for configuration data and secrets management, often used as a lighter-weight alternative to Secrets Manager for configuration values (Secrets Manager adds automatic rotation and is more purpose-built for secrets specifically).

**Exam angle / gotchas:**
- Distinguish **users** (long-term credentials, tied to a person/app) from **roles** (temporary credentials, assumed as needed) — AWS best practice strongly favors roles wherever feasible, including for EC2 instances needing to call other AWS services (never hard-code credentials on an instance).
- Know the *specific* root-only tasks (closing the account, changing support plan, etc.) since these show up directly as exam questions.
- IAM Identity Center is the *preferred, modern* way to manage human access across multiple accounts (vs. creating individual IAM users in every account) — expect this contrast tested directly.
- Secrets Manager vs. Systems Manager Parameter Store: Secrets Manager costs more but offers native automatic rotation for things like database credentials; Parameter Store is well suited for general configuration data and simple secrets and has a free tier.

## Task Statement 2.4 — Security Components and Resources

**AWS security features and services (beyond those in 2.2):**
- **AWS WAF (Web Application Firewall):** protects web applications from common web exploits (e.g., SQL injection, cross-site scripting) by letting you configure rules that allow, block, or monitor (count) web requests based on conditions you define; typically deployed in front of CloudFront, an Application Load Balancer, or API Gateway.
- **AWS Firewall Manager:** a central security management service that lets you configure and manage firewall rules (WAF rules, Shield Advanced protections, VPC security groups, and more) consistently across multiple accounts and resources in an AWS Organization.
- **AWS Shield:** (see 2.2) DDoS protection, Standard (free, automatic) and Advanced (paid, enhanced).
- **Amazon GuardDuty:** (see 2.2) threat detection.

**Third-party security products:** available through **AWS Marketplace**, which offers software (including many security tools — firewalls, endpoint protection, SIEM tools) from third-party vendors that can be deployed directly into a customer's AWS environment, often with consolidated billing through AWS.

**Where AWS security information is available:**
- **AWS Knowledge Center:** a repository of the most frequently requested answers to AWS account and billing/service questions.
- **AWS Security Center:** a hub of security-related resources, best practices, and information about AWS's security approach.
- **AWS Security Blog:** ongoing articles about new security features, best practices, and threat information.

**AWS Trusted Advisor:** an online tool that provides real-time guidance to help provision resources following AWS best practices, across five categories: **cost optimization, performance, security, fault tolerance, and service limits**. For security specifically, Trusted Advisor can flag things like open security group ports, MFA not enabled on the root account, or S3 buckets with open access. The number/depth of checks available depends on the AWS Support plan (Basic/Developer see a limited set of core checks; Business and Enterprise plans unlock the full set of checks).

**Exam angle / gotchas:**
- WAF operates at the *application layer* (Layer 7) filtering HTTP/S requests based on rules; Shield operates against *network/transport layer (Layer 3/4)* and some Layer 7 DDoS attacks (Shield Advanced extends more into Layer 7). Don't confuse "blocking malicious HTTP requests" (WAF) with "protecting against volumetric DDoS floods" (Shield).
- Firewall Manager is about **centrally managing** security rules across many accounts/resources — not a firewall itself.
- Trusted Advisor spans five pillars (cost, performance, security, fault tolerance, service limits) — a scenario asking about "checking for open ports," "checking for unused Elastic IPs," or "checking for service limit approaching" all point to Trusted Advisor.

---

# DOMAIN 3: Cloud Technology and Services (34%)

## Task Statement 3.1 — Methods of Deploying and Operating in AWS

**Ways to provision/access AWS services:**
- **AWS Management Console:** the web-based graphical user interface — best for one-off tasks, exploration, learning, and visual monitoring, but not efficient or repeatable for large-scale/automated operations.
- **AWS Command Line Interface (AWS CLI):** a unified tool for scripting and automating interactions with AWS services from a terminal — good for repeatable tasks and integrating AWS actions into shell scripts.
- **Software Development Kits (SDKs):** language-specific libraries (Python/Boto3, Java, JavaScript, .NET, etc.) that let developers call AWS APIs directly from application code.
- **APIs:** the underlying programmatic interface that the Console, CLI, and SDKs all ultimately call — direct API calls are also possible for custom integrations.
- **Infrastructure as Code (IaC):** defining and provisioning infrastructure through machine-readable definition files rather than manual processes. **AWS CloudFormation** is AWS's native IaC service, using JSON/YAML templates to describe and repeatably deploy a "stack" of resources. IaC is the best choice when you need consistent, version-controlled, repeatable, auditable infrastructure deployments.

**One-time operations vs. repeatable processes:**
- One-time/ad hoc tasks (e.g., a single manual investigation, a one-off resource check) are often fine via the Console.
- Repeatable, scalable, or frequently-changing processes should use CLI, SDKs, or (best for full environments) IaC — this reduces human error, increases speed, and ensures consistency across environments (e.g., dev/test/prod parity).

**Cloud deployment models:**
- **Cloud (all in):** the entire application runs fully in the cloud, built using cloud-native components; a company migrates its existing applications to the cloud or designs/builds new applications in the cloud, generally without maintaining on-premises infrastructure for that workload.
- **Hybrid:** connects cloud-based resources to on-premises infrastructure, extending and growing the on-premises infrastructure — a common approach during migrations or for organizations with regulatory/latency needs that require some infrastructure to remain on-premises (connected via AWS Direct Connect or VPN).
- **On-premises (also called "private cloud"):** deploying resources using virtualization and resource management tools within a company's own data center — sometimes used to describe an organization applying cloud-like management tools to on-prem resources but without the underlying elastic, publicly-shared infrastructure of a true public cloud.

**Exam angle / gotchas:**
- If a scenario needs "consistent, repeatable, version-controlled" environment deployment → IaC/CloudFormation is almost always the right answer, not the Console.
- Distinguish hybrid (cloud + persistent on-prem infrastructure, connected together) from a temporary migration state — hybrid is a deliberate, ongoing architecture choice, often for compliance, latency, or gradual migration reasons.

## Task Statement 3.2 — AWS Global Infrastructure

**Core building blocks:**
- **AWS Region:** a physical geographic location in the world (e.g., us-east-1 in Northern Virginia) that contains multiple, isolated Availability Zones. Each Region is completely independent, which contains and isolates faults, and also helps meet data sovereignty/residency requirements since customers choose which Region(s) their data lives in.
- **Availability Zone (AZ):** one or more discrete data centers with redundant power, networking, and connectivity, housed in separate facilities within a Region. Each Region has multiple AZs (typically 3 or more). **AZs within a Region are connected via high-bandwidth, low-latency private networking**, but are physically separated enough that they **do not share single points of failure** (e.g., power, cooling, flooding risk) — this is what allows synchronous replication across AZs while still providing fault isolation.
- **Edge locations:** sites used by Amazon CloudFront (AWS's CDN) and other services to cache content and serve it to end users with lower latency; there are far more edge locations than Regions/AZs, and they are typically located in major cities around the world, closer to end users than a full Region.
- **Local Zones and Wavelength Zones** (supplementary infrastructure, may appear in scenario questions): Local Zones place compute/storage closer to large population/industry centers for very low-latency use cases; Wavelength Zones embed AWS infrastructure within telecom providers' 5G networks for ultra-low-latency mobile applications.

**High availability via multiple AZs:** by deploying an application's resources (e.g., EC2 instances behind a load balancer, or a Multi-AZ RDS database) across two or more AZs within a Region, an application can continue operating even if an entire AZ becomes unavailable — this is the standard pattern for achieving high availability on AWS.

**When to use multiple Regions:**
- **Disaster recovery (DR) / business continuity:** replicate critical workloads/data to a second, geographically distant Region so the business can recover if an entire Region (or the geography around it) is affected by a large-scale event.
- **Low latency for end users:** deploy the application closer to users in different parts of the world to reduce the round-trip time and improve their experience.
- **Data sovereignty / legal/regulatory requirements:** some laws require that certain categories of data physically reside within a specific country or geographic boundary, requiring you to run infrastructure in a Region located there.
- Additional reasons that may appear: to support specific AWS services only available in certain Regions, or to isolate workloads/accounts by geography for organizational/compliance reasons.

**Exam angle / gotchas:**
- The relationship hierarchy is: **Region → contains multiple Availability Zones → each AZ contains one or more data centers.** Edge locations are a separate, much more numerous layer used for content delivery/caching, not for hosting your primary compute workloads.
- "AZs do not share single points of failure" is a specifically named exam skill — expect a question testing whether you understand that a single power/network/facility failure will not simultaneously take down two AZs in the same Region.
- Don't confuse "more AZs = more Regions" — a single Region contains multiple AZs; you don't need multiple Regions just to achieve basic high availability within one geography.

## Task Statement 3.3 — AWS Compute Services

**Amazon EC2 (Elastic Compute Cloud):** resizable virtual servers ("instances") in the cloud. EC2 instance types are grouped into families optimized for different workloads:
- **General purpose** (e.g., M-family, T-family): balanced compute, memory, and networking — good default choice for web servers, small/medium databases, dev environments.
- **Compute optimized** (e.g., C-family): high-performance processors, best for compute-bound workloads like high-performance web servers, scientific modeling, batch processing, and media transcoding.
- **Memory optimized** (e.g., R-family, X-family): designed for workloads that process large data sets in memory, such as high-performance databases and real-time big-data analytics.
- **Storage optimized** (e.g., I-family, D-family): designed for workloads requiring high, sequential read/write access to very large data sets on local storage, such as NoSQL databases and data warehousing.
- **Accelerated computing** (e.g., P-family, G-family): use hardware accelerators (GPUs) for tasks like machine learning training/inference, graphics processing, and high-performance computing.

**Container services:**
- **Amazon Elastic Container Service (Amazon ECS):** a fully managed container orchestration service using AWS's own native orchestration technology — simpler to get started with if you don't need full Kubernetes compatibility.
- **Amazon Elastic Kubernetes Service (Amazon EKS):** a managed service for running the open-source Kubernetes orchestration platform on AWS — the right choice for organizations that specifically need/want standard Kubernetes (e.g., for portability, existing Kubernetes expertise, or multi-cloud consistency).
- **Amazon Elastic Container Registry (Amazon ECR):** a fully managed Docker/OCI container image registry for storing, managing, and deploying container images (used alongside ECS/EKS).
- Both ECS and EKS can run containers on **EC2** (you manage the underlying instances) or on **AWS Fargate** (serverless — no instance management).

**Serverless compute:**
- **AWS Lambda:** run code without provisioning or managing servers — you upload code (a "function"), and Lambda automatically runs and scales it in response to triggers/events (e.g., an S3 upload, an API Gateway request, a scheduled event), billing only for the compute time actually consumed (down to the millisecond). Ideal for event-driven, short-duration workloads.
- **AWS Fargate:** a serverless compute engine specifically for containers, used with ECS or EKS — you define the container's resource needs (CPU/memory) and Fargate runs it without you provisioning or managing any underlying EC2 instances.

**Elasticity via Auto Scaling:** **AWS Auto Scaling** (and the underlying EC2 Auto Scaling groups) automatically adjusts the number of compute resources (e.g., EC2 instances) up or down based on demand (defined by scaling policies tied to metrics like CPU utilization), ensuring the application has the capacity it needs while avoiding paying for unused, idle capacity — this is the primary technical mechanism that delivers the "elasticity" benefit described in Domain 1.

**Load balancers:** **Elastic Load Balancing (ELB)** automatically distributes incoming application traffic across multiple targets (e.g., EC2 instances, containers, IP addresses) in one or more Availability Zones. Purposes: improve fault tolerance (route around unhealthy targets via health checks), improve availability (spread traffic across AZs), and enable elastic scaling (works with Auto Scaling to distribute load across a dynamically changing fleet). Types include the Application Load Balancer (Layer 7/HTTP), Network Load Balancer (Layer 4, ultra-high performance), and Gateway Load Balancer (for third-party virtual appliances).

**Other compute services worth knowing:**
- **AWS Elastic Beanstalk:** a Platform-as-a-Service-style offering — you upload your application code, and Elastic Beanstalk automatically handles the deployment details (capacity provisioning, load balancing, auto scaling, health monitoring) while still giving you access to the underlying resources if needed.
- **Amazon Lightsail:** a simplified service bundling compute, storage, and networking into an easy, predictable-monthly-price package — designed for simple workloads, small websites, and users who want an easier on-ramp than raw EC2/VPC configuration.
- **AWS Outposts:** brings native AWS infrastructure, services, and APIs to virtually any on-premises or edge location — for customers needing low-latency access to on-prem systems or local data processing while still using the AWS operating model.
- **AWS Batch:** fully manages the provisioning of compute resources to run batch computing jobs (jobs that run to completion without user interaction) at any scale, without needing to install/manage batch processing software.

**Exam angle / gotchas:**
- A scenario mentioning "GPU," "machine learning training," or "graphics rendering" → accelerated computing instance family.
- "High, sequential disk I/O," "NoSQL database," "data warehousing" → storage optimized.
- "In-memory database," "real-time big data processing" → memory optimized.
- ECS vs. EKS: if the scenario specifically mentions **Kubernetes**, the answer is EKS; if it just says "containers" generically with no Kubernetes requirement, ECS is often the simpler/preferred answer.
- Lambda vs. Fargate: Lambda runs discrete **functions** (code, typically short-lived, event-triggered); Fargate runs **containers** (often longer-running application workloads) without server management — both are "serverless" but at different levels of abstraction.
- Auto Scaling = elasticity; Load Balancing = traffic distribution across healthy targets — these often work together but test different concepts.

## Task Statement 3.4 — AWS Database Services

**EC2-hosted (self-managed) databases vs. AWS managed databases:**
- Running a database yourself on EC2 gives you full control over the OS, database engine version/configuration, and any customization — but you are responsible for installation, patching, backups, high availability, and scaling.
- **AWS managed database services** (RDS, DynamoDB, Aurora, etc.) offload most/all administrative burden (patching, backups, replication, failover) to AWS, letting you focus on schema design and queries. **Choose EC2-hosted when you need full OS/engine-level control or run a database engine not supported by a managed offering; choose managed when you want to minimize operational overhead** — this trade-off is a frequently tested decision point.

**Relational databases (SQL):**
- **Amazon RDS (Relational Database Service):** a managed service supporting multiple relational database engines (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server) — handles patching, backups, and (with Multi-AZ deployments) automatic failover to a standby replica in a different AZ for high availability.
- **Amazon Aurora:** AWS's own MySQL- and PostgreSQL-compatible relational database engine, built for the cloud — offers up to 5x the throughput of standard MySQL and 3x that of standard PostgreSQL (per AWS's stated figures), with storage that automatically scales up to 128 TiB and replicates data six ways across three AZs by default for very high durability and availability.

**NoSQL databases:**
- **Amazon DynamoDB:** a fully managed, serverless key-value and document NoSQL database delivering single-digit-millisecond performance at virtually any scale — ideal for applications needing extremely high scalability and low, consistent latency (e.g., gaming leaderboards, shopping carts, IoT data), where data access patterns are typically simple lookups rather than complex joins.
- Other NoSQL-family services mentioned in scope: **Amazon DocumentDB** (MongoDB-compatible document database) and **Amazon Neptune** (graph database, for highly connected data like social networks or recommendation engines).

**Memory-based (in-memory) databases:**
- **Amazon ElastiCache:** a managed in-memory caching service (supporting Redis or Memcached engines) used to significantly speed up application/database performance by caching frequently accessed data in memory, reducing the load on primary databases and reducing latency for read-heavy workloads.

**Database migration tools (also covered in Domain 1's migration content):**
- **AWS Database Migration Service (AWS DMS):** migrates databases to AWS reliably and with minimal downtime, keeping the source database operational throughout most of the migration process; supports both one-time migrations and ongoing replication.
- **AWS Schema Conversion Tool (AWS SCT):** used for heterogeneous migrations (different source and target database engines) to automatically convert the database schema and code objects to the target engine's format before using DMS to migrate the actual data.

**Exam angle / gotchas:**
- If a scenario needs **complex relational queries/joins and ACID transactions** → RDS or Aurora. If it needs **massive scale, simple key-based lookups, and predictable low latency** → DynamoDB.
- If a scenario is about **speeding up read performance / reducing database load via caching** → ElastiCache.
- If a scenario mentions migrating a database **with minimal downtime** → DMS; if it also mentions converting **between two different database engines** → add SCT.
- Aurora is *always* MySQL- or PostgreSQL-compatible — it is not a distinct SQL dialect of its own, and it is not a NoSQL database.

## Task Statement 3.5 — AWS Network Services

**Amazon VPC (Virtual Private Cloud)** — a logically isolated virtual network within AWS where you launch resources; you control its IP address range, subnets, route tables, and network gateways.

**Core VPC components:**
- **Subnets:** subdivisions of a VPC's IP address range, tied to a specific Availability Zone. A **public subnet** has a route to an internet gateway (resources can be reached from/reach the internet); a **private subnet** does not have a direct route to the internet.
- **Internet Gateway (IGW):** allows communication between resources in a VPC and the internet; attached to a VPC and referenced in route tables for public subnets.
- **NAT Gateway:** allows resources in a *private* subnet to initiate outbound connections to the internet (e.g., for software updates) while preventing unsolicited inbound connections from the internet.
- **Route tables:** control where network traffic from a subnet or gateway is directed.
- **VPC Peering:** connects two VPCs privately so resources can communicate as if they were on the same network.

**Security in a VPC:**
- **Security groups:** act as a virtual firewall at the *instance* level — **stateful** (if you allow inbound traffic, the corresponding outbound response is automatically allowed, and vice versa); you can only specify "allow" rules, not explicit "deny" rules.
- **Network Access Control Lists (network ACLs):** act as a firewall at the *subnet* level — **stateless** (inbound and outbound rules are evaluated independently, so return traffic must be explicitly allowed); support both "allow" and explicit "deny" rules, and rules are evaluated in numbered order.
- **Amazon Inspector:** (also in Domain 2) automatically assesses EC2 instances, container images, and Lambda functions for unintended network exposure and software vulnerabilities — relevant to VPC security as it can flag overly permissive network configurations.

**Amazon Route 53:** AWS's highly available and scalable **Domain Name System (DNS)** web service. Purposes include: domain registration, DNS routing (translating human-readable domain names to IP addresses), and health checking (routing traffic away from unhealthy endpoints). Supports advanced routing policies (e.g., latency-based routing, geolocation routing, weighted routing, failover routing).

**Network connectivity options to AWS (hybrid connectivity):**
- **AWS Site-to-Site VPN:** creates an encrypted connection between your on-premises network (or another cloud) and your AWS VPC over the public internet — quick to set up, but subject to the variability/latency of the public internet.
- **AWS Client VPN:** a managed client-based VPN service allowing individual users to securely connect to AWS resources and on-premises networks from anywhere using an OpenVPN-based client.
- **AWS Direct Connect:** establishes a **dedicated, private physical network connection** between your on-premises data center/office and AWS, bypassing the public internet entirely — provides more consistent network performance, higher bandwidth options, and often lower data transfer costs for large, steady workloads compared to internet-based connections; typically takes longer to provision than a VPN.
- Additional networking services worth recognizing: **AWS Transit Gateway** (a central hub to connect multiple VPCs and on-premises networks, simplifying network topology), **AWS Global Accelerator** (improves availability/performance of applications by routing traffic through the AWS global network to the optimal endpoint), **AWS PrivateLink** (provides private connectivity between VPCs and services without exposing traffic to the public internet), and **Amazon CloudFront** (AWS's global Content Delivery Network, caching content at edge locations closer to end users to reduce latency).

**Exam angle / gotchas:**
- Security groups vs. NACLs is one of the most heavily tested Domain 3 comparisons: **security group = stateful, instance-level, allow rules only; NACL = stateless, subnet-level, allow AND deny rules, ordered/numbered.**
- Direct Connect vs. VPN: Direct Connect = dedicated private physical line (consistent performance, longer to set up, often used for large/steady enterprise workloads); VPN (Site-to-Site) = encrypted tunnel over the public internet (fast/easy to set up, more variable performance).
- Route 53's core purpose is DNS — don't confuse it with a load balancer, though it can perform health checks and failover routing that complement load balancing.

## Task Statement 3.6 — AWS Storage Services

**Object storage:**
- **Amazon S3 (Simple Storage Service):** stores data as objects within buckets; virtually unlimited scalability; designed for 99.999999999% (11 nines) durability. Use cases: static website hosting, data lakes, backup/archive, storing unstructured data, distributing large media files.
- **S3 storage classes** (differ mainly by access frequency, retrieval time, durability, and cost):
  - **S3 Standard:** for frequently accessed data; low latency and high throughput; highest cost per GB among the "active" tiers.
  - **S3 Intelligent-Tiering:** automatically moves objects between access tiers based on changing access patterns, without performance impact or operational overhead — good when access patterns are unknown or unpredictable.
  - **S3 Standard-IA (Infrequent Access):** lower storage cost than Standard, but a retrieval fee; for data accessed less frequently but needing rapid access when required.
  - **S3 One Zone-IA:** like Standard-IA but stored in only a single AZ (lower cost, lower resilience) — suited to infrequently accessed, re-creatable data.
  - **S3 Glacier Instant Retrieval:** for archive data that is rarely accessed but still needs millisecond retrieval.
  - **S3 Glacier Flexible Retrieval:** lower-cost archival storage with retrieval times ranging from minutes to hours.
  - **S3 Glacier Deep Archive:** S3's lowest-cost storage class, meant for long-term retention (e.g., 7–10+ years) rarely (perhaps once or twice a year) accessed data, with retrieval times typically measured in hours.

**Block storage:**
- **Amazon Elastic Block Store (Amazon EBS):** provides persistent block-level storage volumes for use with EC2 instances — data persists independently of the life of the instance (unless explicitly configured otherwise), and volumes can be snapshotted to S3 for backup. Suited for workloads needing a traditional file-system-like, low-latency block device (e.g., a database's primary storage, a boot volume).
- **Instance store:** provides temporary block-level storage that is physically attached to the host computer running an EC2 instance — offers very high I/O performance but data is **ephemeral** (lost when the instance is stopped, terminated, or fails) — suited only for temporary/cache data, buffers, or data replicated elsewhere.

**File storage:**
- **Amazon Elastic File System (Amazon EFS):** a fully managed, scalable **NFS (Network File System)** that can be mounted concurrently by multiple EC2 instances (and other compute resources) at once — well suited for shared content repositories, web-serving farms, and workloads needing a common, POSIX-compliant file system across many instances simultaneously.
- **Amazon FSx:** provides fully managed third-party file systems, optimized for specific use cases — **FSx for Windows File Server** (native Windows file shares using the SMB protocol, for Windows-based applications) and **FSx for Lustre** (a high-performance file system for compute-intensive workloads like machine learning and high-performance computing).

**Cached/hybrid file systems:**
- **AWS Storage Gateway:** a hybrid cloud storage service connecting on-premises environments to AWS storage — presents cloud storage locally via standard protocols, with local caching for frequently accessed data. Three main gateway types: **File Gateway** (NFS/SMB access to objects in S3), **Volume Gateway** (block storage volumes backed by S3, with local caching or fully stored copies), and **Tape Gateway** (a virtual tape library interface for backup software, backed by S3/Glacier — enabling a smooth transition away from physical backup tapes).

**Lifecycle policies:** **S3 Lifecycle policies** automatically transition objects between storage classes (e.g., from Standard to Standard-IA to Glacier) or expire/delete them after a defined period, based on rules you configure — used to optimize storage cost automatically over an object's lifetime without manual intervention.

**AWS Backup:** a fully managed, centralized backup service that lets you automate and consolidate backup management across multiple AWS services (EBS, RDS, DynamoDB, EFS, and more) and even on-premises/hybrid resources, from a single console, including centralized backup policies and retention/compliance reporting.

**Exam angle / gotchas:**
- Object storage (S3) is for unstructured *objects* accessed over HTTP/API; block storage (EBS/instance store) is for low-level *volumes* attached to a single compute instance (like a virtual hard drive); file storage (EFS/FSx) is for *shared, concurrent, file-system-level* access from multiple instances at once — a very commonly tested three-way distinction.
- Instance store = ephemeral/temporary (data lost on stop/terminate); EBS = persistent (survives independent of instance lifecycle, absent explicit deletion).
- Glacier Instant Retrieval vs. Flexible Retrieval vs. Deep Archive — ordering from *fastest retrieval/higher cost* to *slowest retrieval/lowest cost* is Instant Retrieval → Flexible Retrieval → Deep Archive.
- Storage Gateway is specifically for **hybrid** (on-premises + cloud) scenarios — if a question mentions an on-premises application needing to use S3-backed storage via standard protocols, Storage Gateway is the answer.

## Task Statement 3.7 — AWS AI/ML Services and Analytics Services

**AI/ML services:**
- **Amazon SageMaker AI:** a fully managed service providing the tools to build, train, and deploy machine learning models at scale, covering the full ML lifecycle (data labeling, notebook environments, training, tuning, hosting/inference).
- **Amazon Lex:** a service for building conversational interfaces (chatbots and voice bots) using the same deep learning technology (automatic speech recognition and natural language understanding) that powers Amazon Alexa.
- **Amazon Comprehend:** a natural language processing (NLP) service that uses machine learning to find insights in text (e.g., sentiment analysis, entity recognition, key phrase extraction, language detection).
- **Amazon Rekognition:** adds image and video analysis to applications (e.g., object/scene detection, facial analysis/comparison, text-in-image detection).
- **Amazon Polly:** turns text into lifelike speech (text-to-speech).
- **Amazon Transcribe:** automatic speech-to-text (transcription) service.
- **Amazon Translate:** a neural machine translation service for translating text between languages.
- **Amazon Textract:** automatically extracts text, handwriting, and data (including from tables and forms) from scanned documents, going beyond simple optical character recognition (OCR).
- **Amazon Q:** AWS's generative-AI-powered assistant, with variants for business users (answering questions, summarizing, generating content based on company data) and for developers (e.g., assisting with code within IDEs and the AWS console).

**Analytics services:**
- **Amazon Athena:** an interactive, serverless query service that lets you analyze data directly in Amazon S3 using standard SQL — no infrastructure to manage, and you pay only for the queries you run.
- **Amazon Kinesis:** a family of services for collecting, processing, and analyzing real-time, streaming data at scale (e.g., clickstreams, IoT telemetry, log data) — enabling near-real-time analytics rather than waiting for batch processing.
- **AWS Glue:** a fully managed **extract, transform, and load (ETL)** service that discovers, prepares, and combines data for analytics, machine learning, and application development — includes the AWS Glue Data Catalog, a central metadata repository.
- **Amazon QuickSight:** a cloud-native, serverless **business intelligence (BI)** service for building interactive dashboards and visualizations, with pay-per-session pricing options.
- **Amazon Redshift:** a fully managed, petabyte-scale **data warehouse** service optimized for complex analytical (OLAP-style) queries across large volumes of structured, historical data.
- **Amazon EMR (Elastic MapReduce):** a managed big-data platform for running open-source frameworks such as Apache Spark, Hive, and Hadoop, at scale, for large-scale data processing.
- **Amazon OpenSearch Service:** a managed service for deploying, operating, and scaling OpenSearch (a search-and-analytics engine derived from Elasticsearch), commonly used for log analytics, full-text search, and real-time application monitoring.

**Exam angle / gotchas:**
- Match the service to the **task type**: text sentiment/entities → Comprehend; images/video → Rekognition; text-to-speech → Polly; speech-to-text → Transcribe; language translation → Translate; document/form data extraction → Textract; chatbots → Lex; general ML model build/train/deploy → SageMaker AI.
- Athena = SQL queries **directly on data sitting in S3**, serverless, no ETL/loading required first. Redshift = a full **data warehouse** you load data *into* for heavy, repeated analytical workloads. Glue = the **ETL/data preparation** layer that often feeds both. QuickSight = the **visualization/BI dashboard** layer on top of the data.
- Kinesis is specifically about **streaming/real-time** data, distinguishing it from the batch-oriented tools (Glue, EMR, Redshift) — though these often work together in a full pipeline.

## Task Statement 3.8 — Other In-Scope AWS Service Categories

**Application integration** (decoupling application components, messaging):
- **Amazon Simple Queue Service (Amazon SQS):** a fully managed message **queuing** service that lets you decouple and scale distributed application components — messages wait in a queue until a consumer processes them (point-to-point, typically one consumer processes each message).
- **Amazon Simple Notification Service (Amazon SNS):** a fully managed **pub/sub (publish/subscribe)** messaging service — a single published message can "fan out" to many subscribers simultaneously (e.g., email, SMS, Lambda functions, SQS queues) at once, unlike SQS's single-consumer queue model.
- **Amazon EventBridge:** a serverless **event bus** service that makes it easy to connect applications using events from your own apps, integrated SaaS applications, and AWS services, with rules to route events to targets — well suited for building event-driven architectures at scale, often with more complex routing/filtering logic than SNS.
- **AWS Step Functions:** lets you coordinate multiple AWS services into serverless workflows (state machines) to build and update applications quickly (relevant background context, though not explicitly named in the Domain 3.8 task list, it's in-scope per the services list).

**Business applications:**
- **Amazon Connect:** an easy-to-use, cloud-based **contact center (customer service call center)** service.
- **Amazon Simple Email Service (Amazon SES):** a cost-effective, scalable email service for sending and receiving marketing, notification, and transactional email.

**Customer enablement:**
- **AWS Support:** provides a mix of tools and technical support plans (see Domain 4) to help customers build and operate on AWS successfully.

**Developer tools:**
- **AWS CodeBuild:** a fully managed continuous integration service that compiles source code, runs tests, and produces software packages ready for deployment.
- **AWS CodePipeline:** a fully managed continuous delivery service that automates release pipelines for fast and reliable application and infrastructure updates, orchestrating build, test, and deploy stages.
- **AWS X-Ray:** helps developers analyze and debug distributed/microservices applications by tracing requests as they travel through the application, helping identify performance bottlenecks and errors.

**End-user computing:**
- **Amazon WorkSpaces:** a managed, secure **Desktop-as-a-Service (DaaS)** solution providing persistent virtual Windows or Linux desktops for users.
- **Amazon AppStream 2.0:** streams desktop applications (rather than a full desktop) from AWS to any device running a web browser, without needing to rewrite the applications.
- **Amazon WorkSpaces Secure Browser:** provides secure, managed web browser access to internal websites and SaaS web applications without needing a full virtual desktop or agent software installed.

**Frontend web and mobile:**
- **AWS Amplify:** a set of tools and services for building and deploying full-stack web and mobile applications quickly, including frontend hosting and backend integration (auth, APIs, storage).

**IoT (Internet of Things):**
- **AWS IoT Core:** lets connected devices easily and securely interact with cloud applications and other devices — handles device connectivity, message routing, and device management at scale.

**Exam angle / gotchas:**
- SQS vs. SNS vs. EventBridge is a frequently tested trio: **SQS = queue, typically one consumer per message, message persists until processed** (decoupling + buffering); **SNS = pub/sub fan-out to multiple subscribers at once** (broadcast notifications); **EventBridge = event bus with advanced routing/filtering rules, often integrating SaaS and many event sources.**
- WorkSpaces (full persistent virtual **desktop**) vs. AppStream 2.0 (streams individual **applications**, not a full desktop) vs. WorkSpaces Secure Browser (just secure **browser** access, no desktop/app streaming) — match to what the scenario says needs to be delivered to end users.
- If a scenario mentions "call center," "contact center," or "customer service phone/chat," Amazon Connect is almost always the answer.

---

# DOMAIN 4: Billing, Pricing, and Support (12%)

## Task Statement 4.1 — AWS Pricing Models

**EC2 compute purchasing options:**
- **On-Demand Instances:** pay for compute by the second/hour with no long-term commitment — best for short-term, unpredictable workloads, or applications being developed/tested for the first time, where you can't yet predict usage patterns.
- **Reserved Instances (RIs):** commit to a specific instance configuration for a 1-year or 3-year term in exchange for a significant discount (up to ~72% compared to On-Demand) versus On-Demand pricing — best for steady-state, predictable workloads.
  - **Standard RIs:** offer the largest discount but the least flexibility to change instance attributes.
  - **Convertible RIs:** offer a slightly smaller discount than Standard, but allow you to change the instance family/attributes during the term while keeping the RI benefit.
  - RIs can be purchased with **All Upfront**, **Partial Upfront**, or **No Upfront** payment options (more upfront payment = greater discount).
- **Savings Plans:** a flexible pricing model offering lower prices (similar to RI-level discounts) in exchange for a commitment to a consistent amount of usage (measured in $/hour) for a 1- or 3-year term — unlike RIs, Savings Plans automatically apply to usage across instance families/sizes (Compute Savings Plans even apply across EC2, Fargate, and Lambda), offering more flexibility than traditional RIs while still delivering deep discounts.
- **Spot Instances:** let you request spare/unused EC2 capacity at discounts of up to ~90% off On-Demand pricing — AWS can reclaim (interrupt) a Spot Instance with short notice (typically a two-minute warning) when the capacity is needed elsewhere, so Spot is best for fault-tolerant, flexible workloads (e.g., batch processing, big data analytics, CI/CD, stateless web servers) that can handle interruption.
- **Dedicated Hosts:** a physical EC2 server fully dedicated to your use — gives you visibility and control over which physical host your instances run on, and lets you use your own existing, eligible software licenses tied to specific hardware attributes (sockets/cores) for BYOL scenarios; typically the most expensive option, chosen for licensing or compliance reasons.
- **Dedicated Instances:** run on hardware dedicated to a single customer, but (unlike Dedicated Hosts) you don't get visibility/control over the specific physical server placement — chosen when you need physical isolation for compliance reasons but don't need Dedicated Host-level control.
- **Capacity Reservations (On-Demand Capacity Reservations):** reserve compute capacity in a specific AZ for any duration, guaranteeing that capacity will be available when you need it — can be combined with Savings Plans/RIs for a discount, but on their own do not provide a billing discount (they guarantee *capacity*, not lower *cost*).

**Reserved Instance flexibility and behavior in AWS Organizations:**
- Convertible RIs can be exchanged for a different configuration (instance family, OS, tenancy) during the term.
- Within **AWS Organizations**, RI (and Savings Plan) discounts can automatically apply across the *entire organization's* linked accounts by default when a member account has matching, unused usage — allowing the benefit of aggregated purchasing/discount-sharing across many accounts (this can be turned off per account if not desired).

**Data transfer costs:**
- **Inbound (ingress)** data transfer to AWS is generally **free** in almost all cases.
- **Outbound (egress)** data transfer from AWS *to the internet* is generally charged, typically on a tiered basis (more data = lower per-GB cost).
- Data transfer **between AWS Regions** is charged (both a "transfer out" charge from the source Region and often a receiving charge, depending on the services involved).
- Data transfer **within the same Region**, **between AZs**, is typically charged a small per-GB fee in each direction (though transfer within the *same* AZ using private IP addresses is typically free).
- Using a **VPC endpoint** or keeping traffic within the same AZ can help minimize data transfer costs.

**Storage pricing options and tiers:** (see Domain 3.6 for the technical description) — generally, storage pricing scales with (a) amount of data stored, (b) how frequently it's accessed/retrieved (colder/archival tiers cost less to store but more/slower to retrieve), and (c) the number of requests made against the data.

**Exam angle / gotchas:**
- Match workload characteristics to purchasing option: **steady-state/predictable → RIs or Savings Plans; unpredictable/short-term → On-Demand; interruptible/flexible/fault-tolerant → Spot; specific physical server / license compliance needs → Dedicated Host; need guaranteed capacity without needing a discount → Capacity Reservation.**
- Remember: **inbound data transfer is (almost always) free; outbound data transfer is what gets charged**, and it typically gets cheaper on a per-GB basis as volume increases (tiered pricing).
- Savings Plans are generally considered more *flexible* than traditional Standard RIs because they apply automatically across instance families/regions/services (for Compute Savings Plans) rather than being locked to one specific instance configuration.

## Task Statement 4.2 — Resources for Billing, Budget, and Cost Management

- **AWS Budgets:** lets you set custom cost and usage budgets that alert you (via email/SNS) when your actual or forecasted costs/usage exceed (or are about to exceed) your defined thresholds — proactive, alert-based cost control.
- **AWS Cost Explorer:** a visualization and analysis tool that lets you view, analyze, and understand your AWS costs and usage over time (historical trends, filtering/grouping by service, account, tag, etc.), and also provides rightsizing/Savings Plans recommendations — more focused on analysis/visibility than proactive alerting.
- **AWS Pricing Calculator:** lets you estimate the cost of AWS services *before* you use them, by modeling out planned architectures — useful for proposals, budgeting, and comparing configurations, without needing an active AWS account.
- **AWS Organizations:** lets you centrally manage and govern multiple AWS accounts as your business scales — key billing feature is **consolidated billing**, which combines usage from all member accounts to potentially reach volume pricing tiers/discounts faster, while still providing a single bill (and the ability to view costs broken out per account) for the whole organization.
- **AWS Cost and Usage Report (CUR):** the most comprehensive, granular billing dataset AWS offers — a detailed report of your costs and usage, delivered to an S3 bucket, that can be further analyzed with tools like Amazon Athena or Amazon QuickSight, or loaded into a data warehouse like Redshift.
- **Cost allocation tags:** key-value tags applied to AWS resources that let you categorize and track costs across dimensions relevant to your business (e.g., by project, department, environment) — these tags then appear as categorization/filtering columns in Cost Explorer and the Cost and Usage Report, enabling detailed cost breakdowns (chargeback/showback) that wouldn't otherwise be possible from a single aggregated bill.

**Exam angle / gotchas:**
- Budgets = **proactive alerting** ("tell me when I'm about to exceed X"); Cost Explorer = **retrospective/analytical visibility** ("show me and help me understand what I've already spent"). This distinction (forward-looking alert vs. backward-looking analysis) is commonly tested.
- Pricing Calculator is used **before** deploying anything (an estimation tool) — it does not read your actual account usage.
- Consolidated billing (via AWS Organizations) is about combining billing/volume discounts across many accounts into one bill — not about security or access management (that's a separate Organizations feature, Service Control Policies, which is outside Domain 4's scope but sometimes conflated).

## Task Statement 4.3 — AWS Technical Resources and Support Options

**Where to find AWS documentation/guidance:**
- **AWS Knowledge Center:** answers to the most frequently requested account and billing questions.
- **AWS Prescriptive Guidance:** strategies, guides, and patterns to help customers implement AWS solutions using AWS's own best practices, faster.
- **AWS re:Post:** a cloud knowledge service / Q&A community where customers can find and share answers to AWS questions (an AWS-managed, crowd-sourced/expert-supported community resource, replacing the older AWS Forums).
- General resources: whitepapers, blogs, and official documentation on the AWS website provide deep-dive technical and best-practice guidance across all service areas.

**AWS Support plans (from least to most comprehensive):**
- **Basic Support:** free for all AWS customers; includes access to whitepapers/documentation/support forums (re:Post), the Personal Health Dashboard, and a limited set of AWS Trusted Advisor checks (core/basic checks). No technical support cases with AWS engineers.
- **Developer Support:** paid plan intended for those experimenting/testing in AWS; adds business-hours email access to Cloud Support Associates and general architectural guidance.
- **Business Support:** paid plan intended for production workloads; adds 24/7 phone/chat/email access to Cloud Support Engineers, faster response times, full set of Trusted Advisor checks, and access to the AWS Infrastructure Event Management for an additional fee.
- **AWS Enterprise On-Ramp Support:** a mid-tier enterprise plan for customers beginning to run production/business-critical workloads, providing a pool of Technical Account Managers (TAM) and faster response times than Business Support, at a lower cost than full Enterprise Support.
- **Enterprise Support:** the highest tier, for business- and mission-critical workloads; adds a **dedicated Technical Account Manager (TAM)**, concierge support team access, the fastest response times (including a 15-minute response time target for the most urgent, business-critical cases), and proactive guidance/reviews.
- All paid plans build on the tier below them, adding progressively faster response times and more proactive/dedicated resources.

**AWS Support Center:** the central hub within the AWS Management Console for creating and managing support cases, accessing Trusted Advisor, and viewing account health.

**Other support/monitoring tools:**
- **AWS Trusted Advisor:** (also Domain 2) provides recommendations across cost optimization, performance, security, fault tolerance, and service limits; depth of checks scales with Support plan tier.
- **AWS Health Dashboard:** provides alerts and remediation guidance when AWS is experiencing events that may affect you — the *account-specific* view (AWS Health Dashboard) shows issues relevant to your specific resources, distinct from the public **Service Health Dashboard**, which shows the general operational status of AWS services overall.
- **AWS Health API:** allows programmatic access to the same AWS Health event data (for integrating health/operational alerts into your own tools).

**AWS Trust and Safety team:** the team to contact/report to for abuse of AWS resources (e.g., if you discover an AWS-hosted resource being used for phishing, malware distribution, spam, or other abuse of AWS services) — distinct from a standard technical support case.

**AWS Partner Network (APN) and AWS Marketplace:**
- **AWS Partner Network (APN):** a global program of AWS Partners — including **independent software vendors (ISVs)** (who build software solutions that run on/integrate with AWS) and **system integrators (SIs)** (consulting-style partners who help customers design, build, and manage workloads on AWS).
- Benefits of being an AWS Partner: access to partner training and certification, participation in partner events, and eligibility for partner volume discounts, among other program benefits.
- **AWS Marketplace:** a curated digital catalog where customers can find, buy, deploy, and manage third-party software (and data products) that runs on AWS — key capabilities include simplified procurement/licensing, cost management, and governance/entitlement tracking for purchased software, often with billing consolidated into the customer's regular AWS bill.

**Technical assistance options:**
- **AWS Professional Services:** a global team of consultants who help enterprises achieve specific outcomes related to cloud adoption, working alongside AWS Partners.
- **AWS Solutions Architects:** AWS technical experts who help design and guide well-architected solutions for customers (often engaged as part of the sales/support relationship or via Professional Services engagements).

**Exam angle / gotchas:**
- Memorize the **support plan hierarchy and their distinguishing features**: Basic (free, self-service only) → Developer (business-hours email, one primary contact) → Business (24/7, all support channels, full Trusted Advisor) → Enterprise On-Ramp (pool of TAMs) → Enterprise (dedicated TAM, fastest response, concierge).
- AWS Health Dashboard (**your account's** specific events) vs. Service Health Dashboard (**AWS-wide, public** operational status) is a frequently tested distinction.
- ISV vs. system integrator: ISV = **builds software products**; system integrator = **provides consulting/implementation services** to help customers build/migrate/manage on AWS.
- Reporting abuse of AWS resources goes to the **AWS Trust and Safety team**, not a standard technical support ticket.

---

# Appendix A: Quick-Reference — Full In-Scope AWS Services by Category

- **Analytics:** Amazon Athena, Amazon EMR, AWS Glue, Amazon Kinesis, Amazon OpenSearch Service, Amazon QuickSight, Amazon Redshift
- **Application Integration:** Amazon EventBridge, Amazon SNS, Amazon SQS, AWS Step Functions
- **Business Applications:** Amazon Connect, Amazon SES
- **Cloud Financial Management:** AWS Budgets, AWS Cost and Usage Reports, AWS Cost Explorer, AWS Marketplace
- **Compute:** AWS Batch, Amazon EC2, AWS Elastic Beanstalk, Amazon Lightsail, AWS Outposts
- **Containers:** Amazon ECR, Amazon ECS, Amazon EKS
- **Customer Enablement:** AWS Support
- **Database:** Amazon Aurora, Amazon DocumentDB, Amazon DynamoDB, Amazon ElastiCache, Amazon Neptune, Amazon RDS
- **Developer Tools:** AWS CLI, AWS CodeBuild, AWS CodePipeline, AWS X-Ray
- **End User Computing:** Amazon AppStream 2.0, Amazon WorkSpaces, Amazon WorkSpaces Secure Browser
- **Frontend Web and Mobile:** AWS Amplify
- **IoT:** AWS IoT Core
- **Machine Learning:** Amazon Comprehend, Amazon Lex, Amazon Polly, Amazon Q, Amazon Rekognition, Amazon SageMaker AI, Amazon Textract, Amazon Transcribe, Amazon Translate
- **Management and Governance:** AWS Auto Scaling, AWS CloudFormation, AWS CloudTrail, Amazon CloudWatch, AWS Compute Optimizer, AWS Config, AWS Control Tower, AWS Health Dashboard, AWS License Manager, AWS Management Console, AWS Organizations, AWS Service Catalog, Service Quotas, AWS Systems Manager, AWS Trusted Advisor, AWS Well-Architected Tool
- **Migration and Transfer:** AWS Application Discovery Service, AWS Application Migration Service, AWS DMS, Migration Evaluator, AWS Migration Hub, AWS SCT
- **Networking and Content Delivery:** Amazon API Gateway, Amazon CloudFront, AWS Direct Connect, AWS Global Accelerator, AWS PrivateLink, Amazon Route 53, AWS Transit Gateway, Amazon VPC, AWS VPN, AWS Site-to-Site VPN, AWS Client VPN
- **Security, Identity, and Compliance:** AWS Artifact, AWS Certificate Manager (ACM), AWS CloudHSM, Amazon Cognito, Amazon Detective, AWS Directory Service, AWS Firewall Manager, Amazon GuardDuty, AWS IAM, AWS IAM Identity Center, Amazon Inspector, AWS KMS, Amazon Macie, AWS Resource Access Manager (AWS RAM), AWS Secrets Manager, AWS Security Hub, AWS Shield, AWS WAF
- **Serverless:** AWS Fargate, AWS Lambda
- **Storage:** AWS Backup, Amazon EBS, Amazon EFS, AWS Elastic Disaster Recovery, Amazon FSx, Amazon S3, Amazon S3 Glacier, AWS Storage Gateway

# Appendix B: High-Yield Comparison Tables

**Storage type comparison:**

| Type | Examples | Access pattern | Persistence |
|---|---|---|---|
| Object | Amazon S3 | HTTP/API, unstructured objects | Durable, region-replicated |
| Block | EBS, Instance Store | Attached to one instance, like a virtual disk | EBS persistent; Instance Store ephemeral |
| File | EFS, FSx | Shared, concurrent, POSIX/SMB access from many instances | Persistent, managed |

**Security group vs. Network ACL:**

| Feature | Security Group | Network ACL |
|---|---|---|
| Level | Instance (ENI) | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow and Deny |
| Evaluation | All rules evaluated | Evaluated in numbered order |

**Governance/monitoring trio:**

| Service | Primary purpose |
|---|---|
| Amazon CloudWatch | Performance monitoring, metrics, alarms |
| AWS CloudTrail | API activity logging / auditing (who did what) |
| AWS Config | Resource configuration tracking / compliance history |

**Support plan tiers:**

| Plan | Key feature |
|---|---|
| Basic | Free; self-service resources only |
| Developer | Business-hours email support |
| Business | 24/7 all-channel support; full Trusted Advisor |
| Enterprise On-Ramp | Pool of TAMs |
| Enterprise | Dedicated TAM; fastest response times |

# Appendix C: Common Exam Traps (Cross-Domain)

- **CapEx vs. OpEx:** on-premises = CapEx (upfront, fixed); AWS = OpEx (pay-as-you-go, variable).
- **"OF the cloud" vs. "IN the cloud":** AWS secures the infrastructure; the customer secures their data, access, and configuration.
- **Elasticity ≠ scalability in general:** elasticity specifically implies automatic, rapid, on-demand scaling (Auto Scaling).
- **Region vs. AZ vs. edge location:** Region (geography, contains AZs) → AZ (isolated data center cluster within a Region) → edge location (CDN caching point, far more numerous, not for hosting primary workloads).
- **RI/Savings Plans vs. Spot vs. On-Demand:** predictable/steady → RI/Savings Plans; unpredictable → On-Demand; interruptible/flexible → Spot.
- **Inbound vs. outbound data transfer:** inbound is (almost always) free; outbound to the internet is billed.
- **SQS vs. SNS vs. EventBridge:** queue/one consumer vs. pub-sub fan-out vs. event bus with advanced routing.
- **CloudTrail vs. CloudWatch vs. Config:** audit log vs. performance monitoring vs. configuration history/compliance.
- **GuardDuty vs. Inspector vs. Security Hub:** threat detection vs. vulnerability scanning vs. aggregated findings dashboard.

---

*End of guide. Ready for additional topics/domains to be appended, or for conversion into quiz/flashcard format.*
