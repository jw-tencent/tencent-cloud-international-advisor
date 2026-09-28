# Evidence, Numbers, and Claims Policy

## Evidence labels

Use one label for every decision-relevant claim:

| Label | Meaning | Allowed use |
|---|---|---|
| `VERIFIED` | A current authoritative source directly supports the claim | Customer-facing when cited with scope and conditions |
| `CUSTOMER-PROVIDED` | The customer or user supplied the input, but it is not independently validated | Requirement, baseline, or model input with attribution |
| `ESTIMATE` | A calculation or inference based on explicit assumptions | Planning and scenario analysis with formula and range |
| `UNKNOWN` | Evidence is missing, ambiguous, inaccessible, or requires owner confirmation | Do not convert into a positive claim |

An old note, search snippet, generated answer, unsourced presentation, or static comparison table is not sufficient evidence for `VERIFIED`.

## Source hierarchy

Prefer sources in this order:

1. Signed contract, authorized quote, or customer-specific official confirmation.
2. Current official product documentation, pricing, SLA, API, compliance, lifecycle, and regional-availability pages.
3. Current official competitor documentation for competitor claims.
4. Customer-provided architecture, bills, telemetry, requirements, and written confirmation.
5. Reputable third-party sources, labeled and corroborated when possible.
6. Local notes only as search hints.

Use each vendor's own source to support claims about that vendor.

## Required citation fields

For pricing, performance, SLA, quota, compliance, feature availability, and geographic coverage, record:

- Claim.
- Source title and exact URL.
- Access date.
- Product or service.
- Country, region, and Availability Zone when relevant.
- Version, tier, instance family, protocol, or pricing model when relevant.
- Exceptions, prerequisites, and footnotes.

## Freshness gate

Re-check live official sources for:

- Price, discount, tax, currency, exchange rate, free tier, and billing granularity.
- Region and zone count, service availability, capacity, quota, and instance family.
- SLA, support plan, lifecycle, preview or general-availability status, and feature limits.
- Compliance certification, legal terms, data residency, and cross-border handling.
- Performance numbers and benchmarks.

Treat static snapshots as historical context, not current customer commitments.

## Numerical claims

### VERIFIED numbers

State the source, value, unit, date, scope, and conditions.

```text
VERIFIED — [value and unit] for [service/tier] in [region], [billing mode],
accessed [date]. Source: [exact URL].
```

### ESTIMATE numbers

Show inputs and formula.

```text
ESTIMATE — monthly cost = compute + storage + requests + network + security +
observability + support + estimated operations.
```

Include:

- Baseline.
- Low, base, and high assumptions.
- Excluded costs.
- Sensitivity drivers.
- Validation action.

Never present an estimate as an achieved customer result.

## Competitive claims

Use these states:

- `Verified support`: official documentation confirms the capability in the compared scope.
- `Partial / conditional`: support depends on tier, region, add-on, partner, architecture, or limitation.
- `Not verified`: current research did not establish the claim.
- `Verified unavailable`: official documentation explicitly states that the capability is unavailable in the compared scope.

Failure to find a feature means `Not verified`, not `Verified unavailable`.

Before calling a capability differentiated, check whether competitors deliver the same outcome through another service, architecture, partner, or operating model.

## Compliance and legal claims

- Cite the exact certification, service scope, region, entity, and validity period when available.
- Distinguish provider certification from customer workload compliance.
- Avoid legal conclusions.
- Mark unresolved legal interpretation `UNKNOWN` and route it to the correct owner.
- Never imply that a certified cloud service automatically makes a customer application compliant.

## Claim review checklist

Before external use, confirm:

- Every important number has a source or explicit assumption.
- Every comparison uses equivalent scope and configuration.
- Every better, cheaper, or faster claim defines the metric and test conditions.
- Every unique, only, or unavailable claim has direct evidence across the named alternatives.
- Every source applies to the region, tier, version, and commercial scope being discussed.
- Every unknown has an owner and validation action.
