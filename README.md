# Tencent Cloud International Advisor Skill

A public, customer-facing WorkBuddy skill for questions about Tencent Cloud International products and services.

## What customers can ask

- What a Tencent Cloud service does and when to use it
- Which service fits a workload
- Whether a product, tier, or feature is available in a target region
- How pricing and billing work
- Architecture, migration, reliability, security, and operations guidance
- API and SDK implementation questions
- SLA and compliance questions
- Troubleshooting and official support paths
- Evidence-based comparisons with other cloud providers

## Evidence policy

The skill uses current public official sources and separates:

- `VERIFIED` — supported by current official evidence
- `CUSTOMER-PROVIDED` — supplied by the customer but not independently verified
- `ESTIMATE` — calculated from explicit assumptions
- `UNKNOWN` — requires more evidence or official confirmation

It does not use Tencent internal knowledge bases, unpublished roadmaps, private pricing, customer data, or internal escalation information.

## Important boundaries

- The Global Infrastructure page does not prove product-specific regional availability.
- China mainland and international deployments require separate validation.
- Pricing pages and calculators are not substitutes for an authorized quote.
- Platform certifications do not automatically make a customer's workload compliant.
- This community skill is not an official contractual statement from Tencent Cloud.

## Install

### Upload the ZIP

Upload `tencent-cloud-international-advisor.zip` through the WorkBuddy Skills interface.

### Install from a local folder

Copy the repository folder to:

```text
User scope:    ~/.workbuddy/skills/tencent-cloud-international-advisor/
Project scope: <project>/.workbuddy/skills/tencent-cloud-international-advisor/
```

The folder must contain `SKILL.md` at its root.

## Example requests

```text
What is Tencent Cloud EdgeOne, and when should I use it instead of a traditional CDN?
```

```text
Is Tencent Kubernetes Engine available in Frankfurt? Cite the current product-specific source.
```

```text
Estimate the monthly COS cost for 20 TB stored in Singapore and 8 TB of monthly Internet egress.
Separate current official prices from my workload assumptions.
```

```text
Compare Tencent Cloud CVM and Amazon EC2 for a latency-sensitive API serving Southeast Asia.
Use each provider's official documentation and list proof still required.
```

```text
My Tencent Cloud API call fails. Tell me which sanitized details to collect and how to open a support ticket.
```

## Repository structure

```text
tencent-cloud-international-advisor/
├── SKILL.md
├── README.md
├── LICENSE
├── workbuddy.json
├── references/
│   ├── api_reference.md
│   ├── evidence-policy.md
│   ├── international-checklist.md
│   ├── output-templates.md
│   ├── playbooks.md
│   └── public-release-safety.md
├── scripts/
│   └── example.py
└── assets/
    └── example_asset.txt
```

## Public-use safety

Before adding examples or contributions, follow `references/public-release-safety.md`. Never commit credentials, customer material, private Tencent content, contract pricing, local project paths, or unsupported performance and savings claims.

## License

Apache License 2.0. See `LICENSE`.
