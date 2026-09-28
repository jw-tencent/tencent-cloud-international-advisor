# Customer Response Templates

Use the smallest template that answers the question. Remove unused sections.

## Short Product Answer

```markdown
## Direct answer
[One to three sentences]

## Scope and conditions
- Product/edition:
- Region:
- Important limitation:

## Official source
- [Page title](exact URL) — accessed [date]

## Next step
[Only when customer input or official confirmation is required]
```

## Capability Verification

```markdown
## Result
Supported and verified / Supported with conditions / Not verified / Verified unavailable

## Scope
- Service:
- Edition or tier:
- Region:
- API or feature version:

## Evidence
- Claim:
- Official source:
- Access date:
- Conditions or exceptions:

## Open item
- Item:
- Owner:
- Validation action:
```

## Service Recommendation

```markdown
## Recommendation
[Recommended Tencent Cloud service or pattern]

## Why it fits
- Requirement:
- Match:
- Evidence:

## Conditions and limitations
- Region or edition:
- Scale or quota:
- Integration:
- Operational responsibility:

## Alternatives
- [Alternative and when to use it]

## Information still needed
- CUSTOMER-PROVIDED:
- UNKNOWN:
```

## Region Availability Answer

```markdown
## Direct answer
[Available / available with conditions / not verified / officially unavailable]

## Product-specific evidence
- Service and edition:
- Region and Availability Zone:
- Supported feature or SKU:
- Official source and access date:

## Important distinction
The Global Infrastructure page shows general Tencent Cloud footprint; product-specific availability is determined by the product documentation and current purchase path.

## Confirmation still required
- Account quota:
- Capacity:
- Purchase eligibility:
```

## Pricing Answer

```markdown
## Billing model
- Service:
- Region:
- Currency:
- Billing mode:
- Billable dimensions:

## VERIFIED public prices
| Item | Unit price | Scope and date | Official source |
|---|---:|---|---|

## CUSTOMER-PROVIDED or ESTIMATE inputs
| Input | Value | Type | Rationale |
|---|---:|---|---|

## Estimate
- Formula:
- Low:
- Base:
- High:

## Exclusions
- Tax:
- Discount or voucher:
- Support:
- Network or adjacent services:

## Next step
[Pricing Center, purchase console, or authorized quote]
```

## Architecture Recommendation

```markdown
## Recommendation
[Conclusion first]

## Requirements and assumptions
| Item | Type | Detail |
|---|---|---|
| ... | VERIFIED / CUSTOMER-PROVIDED / ESTIMATE / UNKNOWN | ... |

## Logical architecture
[Traffic flow, data flow, trust boundaries, regions, and zones]

## Tencent Cloud components
| Requirement | Service or pattern | Rationale | Constraint | Evidence |
|---|---|---|---|---|

## Reliability and operations
- Availability:
- RTO and RPO:
- Observability:
- Backup and restore:
- Support:

## Security and compliance
- Identity:
- Network controls:
- Encryption and key management:
- Logging and data residency:

## Risks and validation
| Item | Impact | Validation | Owner |
|---|---|---|---|

## Next step
[PoC, quote, architecture review, or customer decision]
```

## Troubleshooting Answer

```markdown
## Current assessment
[Most likely issue category without claiming an unverified root cause]

## Safe checks
1. ...
2. ...

## Sanitized evidence needed
- Error code and message:
- RequestId:
- Timestamp and time zone:
- Region and endpoint:
- SDK/API/runtime version:
- Minimal reproduction:

## Do not share
SecretId, SecretKey, passwords, tokens, cookies, private keys, unredacted logs, account IDs, or personal information.

## Official sources
- [Troubleshooting or error-code page]

## Escalation
[Official console ticket path when account-side inspection is required]
```

## SLA or Compliance Answer

```markdown
## Direct answer
[Verified statement with scope]

## Scope
- Service:
- Edition:
- Region/entity:
- Measurement or certification period:

## Conditions and exclusions
- ...

## Official evidence
- [Exact SLA or certification page] — accessed [date]

## Responsibility boundary
[Platform responsibility versus customer configuration]

## Required specialist review
[Legal, privacy, security, or contract owner when needed]
```

## Competitive Answer

```markdown
## Customer decision
[What the customer is choosing]

## Normalized scope
- Workload:
- Region:
- Architecture and tier:
- Support and commercial assumptions:

## Evidence-based comparison
| Decision criterion | Tencent Cloud evidence | Competitor evidence | Finding | Proof needed |
|---|---|---|---|---|

## Tencent Cloud fit
- ...

## Competitor strength
- ...

## Safe conclusion
[No unsupported superlatives or exclusivity claims]
```
