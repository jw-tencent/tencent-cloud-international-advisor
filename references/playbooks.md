# Tencent Cloud International Customer Question Playbooks

## 1. Service Overview

Use when a customer asks what a service is or what it does.

1. Identify the exact Tencent Cloud International service.
2. Open the current official product page and Product Introduction documentation.
3. Explain the service in plain language.
4. List common use cases and major decision factors.
5. State important regional, edition, or integration limitations.
6. Link the exact official pages.

Avoid broad marketing claims and avoid listing unrelated products.

## 2. Service Selection

Use when a customer describes a workload but not a specific product.

1. Clarify workload, target users, target regions, data, traffic, availability, security, and operational model.
2. Map requirements to Tencent Cloud service categories.
3. Verify each candidate service on the International product catalog and product documentation.
4. Recommend one primary pattern and explain when alternatives fit better.
5. Identify product availability, quota, capacity, integration, and commercial items that still require confirmation.

Use this table when useful:

| Requirement | Tencent Cloud service or pattern | Why it fits | Condition or limitation | Evidence |
|---|---|---|---|---|

## 3. Region and Availability Verification

1. Confirm the exact product, edition, feature, SKU, and target region.
2. Use the Global Infrastructure page only for general footprint context.
3. Open the product-specific Regions or Supported Regions documentation.
4. Check purchase guide, console availability, or API region information when relevant.
5. Distinguish documented support from current account quota or physical capacity.

Return one of:

- `VERIFIED — Available in the requested scope.`
- `VERIFIED — Available with conditions.`
- `UNKNOWN — Product-specific public evidence is insufficient.`
- `VERIFIED UNAVAILABLE — Official documentation explicitly excludes the requested scope.`

## 4. Pricing and Billing

1. Confirm product, region, tier, billing mode, currency, quantity, duration, and relevant usage dimensions.
2. Open the current product Purchase Guide or Billing documentation.
3. Capture current public price evidence and access date.
4. Label customer usage as `CUSTOMER-PROVIDED` and modeled usage as `ESTIMATE`.
5. Include adjacent costs such as storage, requests, Internet egress, inter-region traffic, security, logs, support, and licenses when material.
6. Show the formula, exclusions, and sensitivity drivers.
7. Route contract pricing, private offers, discounts, and tax questions to an authorized account team.

Never quote a price from model memory or a static local table.

## 5. Architecture Guidance

1. Restate business and technical requirements.
2. List assumptions and unknowns.
3. Verify each proposed service and region.
4. Create a logical architecture covering traffic, data, identity, trust boundaries, availability, observability, backup, and operations.
5. Explain component selection and alternatives.
6. Include risks, validation steps, and responsibility boundaries.

Do not present a conceptual recommendation as a final production design.

## 6. Migration Guidance

1. Capture the current environment, dependencies, data volume, downtime tolerance, RTO, RPO, and rollback requirements.
2. Separate assessment, landing zone, connectivity, data migration, application migration, validation, cutover, and optimization phases.
3. Verify Tencent Cloud target-service compatibility and regional availability.
4. Identify data-transfer, egress, licensing, identity, observability, and operational changes.
5. Build a rollback plan and acceptance criteria.
6. Recommend a PoC when compatibility or performance remains uncertain.

## 7. API and SDK Guidance

1. Identify product, API action, API version, SDK language and version, endpoint, and region.
2. Open the exact official API or SDK page.
3. Explain prerequisites and request flow.
4. Provide code only from the documented parameter and authentication model.
5. Use placeholders or environment variables for credentials.
6. Cite the official API action and SDK guide.

Never invent parameters or request customer credentials.

## 8. Troubleshooting

Collect only sanitized information:

- Product and feature.
- Region and endpoint.
- Timestamp and time zone.
- Error code and message.
- RequestId or trace identifier.
- SDK, API, runtime, or client version.
- Minimal reproduction steps.
- Expected versus actual behavior.
- Recent configuration changes.

Then:

1. Check official error-code, FAQ, troubleshooting, release-note, and status-related documentation.
2. Separate configuration errors from quota, capacity, billing, permission, and backend issues.
3. Provide safe diagnostics and rollback steps.
4. Recommend an official support ticket when account-side inspection is required.

Never request SecretId, SecretKey, passwords, tokens, cookies, private keys, full production logs, or unredacted customer data.

## 9. SLA and Compliance

1. Identify the exact service, edition, region, and customer requirement.
2. Open the service-specific SLA or exact certification page.
3. State measurement method, exclusions, compensation conditions, and scope.
4. Separate provider responsibility from customer configuration responsibility.
5. Mark legal or regulatory interpretation `UNKNOWN` and recommend qualified review.

## 10. Competitive Comparison

1. Confirm the customer workload, target region, incumbent, alternatives, and decision criteria.
2. Normalize architecture, tier, support, commitment, and commercial scope.
3. Research Tencent Cloud from Tencent Cloud official sources.
4. Research each competitor from that competitor's official sources.
5. Classify support as verified, conditional, not verified, or verified unavailable.
6. State both Tencent Cloud strengths and competitor strengths.
7. Define proof required through a benchmark, PoC, product confirmation, or quote.

Do not use absence from search results as proof that a competitor lacks a capability.

## 11. Support and Escalation

Use current public support documentation and the official console ticket entry.

Recommend a ticket when the question requires:

- Account or identity inspection.
- Quota or capacity changes.
- Billing investigation or refund review.
- Backend logs or platform incident analysis.
- Contract, private offer, or service-credit review.
- Product-specific confirmation not available publicly.

Do not expose or fabricate internal escalation contacts or response-time commitments.
