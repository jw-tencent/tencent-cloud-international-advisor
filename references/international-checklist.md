# Tencent Cloud International Customer Checklist

Use only sections relevant to the question. This checklist is not proof of product capability.

## Customer-data handling

- Collect only information needed for the current question.
- Confirm authorization before processing architecture, bills, logs, telemetry, or security evidence.
- Remove credentials, tokens, passwords, personal data, account IDs, public IPs, internal hostnames, contract identifiers, and confidential pricing.
- Keep customer-confidential information out of public search queries and reusable examples.
- Summarize or anonymize evidence when raw data is unnecessary.

## International-site scope

- Confirm that documentation applies to Tencent Cloud International.
- Do not apply China-site pricing, promotions, quotas, or product availability to international customers.
- Preserve official links under `tencentcloud.com`, `www.tencentcloud.com`, or `intl.cloud.tencent.com` when they resolve to Tencent Cloud public pages.
- Note when a page is AI-translated and verify ambiguous customer-critical wording through another official source or support.

## Customer context

- Customer operating countries or regions.
- End-user locations and latency-sensitive markets.
- Industry, regulated data, and critical workloads.
- Current environment, required integrations, and migration constraints.
- Decision date and target production date.
- Technical, security, legal, procurement, and operations stakeholders.

## Regional availability

Verify from current official sources:

- Target region and Availability Zone.
- Product, edition, SKU, instance family, accelerator, feature, and capacity availability.
- Multi-zone and multi-region support.
- Quota and capacity reservation requirements.
- Control-plane, data-plane, backup, log, key, and metadata locations.

Never infer product availability from the Global Infrastructure page alone.

## Data and compliance

Clarify:

- Data classification and regulated data types.
- Data Residency and sovereignty requirements.
- Cross-border transfer restrictions and approved mechanisms.
- Encryption in transit and at rest, customer-managed keys, key location, and rotation.
- Logging, retention, deletion, backup, and eDiscovery requirements.
- Required certifications and exact workload scope.
- Shared-responsibility boundaries.

Treat legal interpretation as `UNKNOWN` until confirmed by a qualified legal or compliance owner.

## Network and performance

Collect:

- Source and destination traffic matrix.
- Peak and average throughput, packets per second, concurrent connections, and growth.
- Protocols, ports, long-lived connections, and UDP, TCP, or QUIC requirements.
- Latency, jitter, packet loss, availability, RTO, and RPO targets.
- Internet, VPN, dedicated connectivity, acceleration, CDN or edge, DDoS, WAF, and DNS needs.
- Ingress, egress, inter-zone, inter-region, origin, and third-party transit costs.
- Client ISP, mobile network, and last-mile test coverage.

Do not promise latency before route-specific measurement.

## Architecture and operations

Confirm:

- Current architecture, dependencies, deployment model, and failure domains.
- Identity federation, role model, least privilege, secrets, and break-glass process.
- Observability, audit, incident response, support escalation, and on-call ownership.
- Backup, restore testing, disaster recovery, and failover process.
- Infrastructure as Code, CI/CD, image, patch, and vulnerability management.
- Team skills, operating model, managed-service preference, and partner requirements.

## Commercial scope

Verify:

- Contracting and billing entity.
- Currency, tax, invoice, payment terms, and purchase channel.
- Pay-as-you-go, subscription, committed use, tiered pricing, or negotiated discount.
- Support plan and professional services.
- Exchange-rate assumption and quote validity.
- Included and excluded products, network charges, licenses, migration, and operations.

Treat calculator output as an estimate, not a formal quote.

## China mainland versus international deployment

Treat these as separate solution tracks. When service to or deployment in the Chinese mainland is required, separately verify product availability, licensing or filing requirements, content and cybersecurity obligations, cross-border connectivity, data transfer, local entity or partner needs, and operational process.

Use 中国香港 / Hong Kong, China; 中国澳门 / Macao, China; 中国台湾 / Taiwan, China.

## Stop conditions

Do not issue a definitive recommendation while a decision-critical item remains unresolved:

- Required product or feature availability in the target region.
- Data residency or regulatory fit.
- Contracting or billing feasibility.
- Critical quota or capacity.
- Required service-specific SLA or support coverage.
- Cross-border network feasibility.
- Customer baseline required for cost or performance claims.

Mark the item `UNKNOWN`, assign an owner, and define the validation action.
