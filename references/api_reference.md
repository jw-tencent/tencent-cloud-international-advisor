# Tencent Cloud International Public Source Map

Use this file to choose the correct public source. Re-open the exact page before answering because URLs, navigation, availability, pricing, and product status can change.

## Core public entry points

| Need | Official public entry point | Usage rule |
|---|---|---|
| Tencent Cloud International homepage | https://www.tencentcloud.com/ | Use for public navigation and current featured services, not as proof of detailed product capability. |
| Product catalog | https://www.tencentcloud.com/product | Use to discover product categories and official product pages. |
| Product documentation | https://www.tencentcloud.com/document/product | Navigate to the exact product documentation. Prefer the product-specific page over a general landing page. |
| API documentation pattern | https://www.tencentcloud.com/document/api/ | Use the exact product and API page. Verify API version, endpoint, region requirement, rate limit, and error-code scope. |
| Global infrastructure | https://www.tencentcloud.com/global-infrastructure | Use for general region and Availability Zone context only. Do not infer product availability. |
| Compliance center | https://www.tencentcloud.com/document/product/363 | Use to locate the exact public certification or audit page and verify scope. |
| General SLA | https://www.tencentcloud.com/document/product/301/12905 | Use as the general framework. For commitments, locate the service-specific SLA. |
| Standard support methods | https://www.tencentcloud.com/document/product/1214/56750 | Use for current public support channels and plan conditions. |
| Console ticket entry | https://console.tencentcloud.com/workorder | Use when account-side inspection or official support is required. |

Official pages may also resolve under `tencentcloud.com` without `www` or under `intl.cloud.tencent.com`. Preserve the official resolved URL when it remains on a Tencent Cloud-controlled domain.

## Source selection by question

### Product overview

1. Start from the Product Catalog.
2. Open the product landing page.
3. Open Product Introduction, Use Cases, or Overview documentation.
4. Cite the exact page that supports the answer.

### Feature support

1. Open the product documentation.
2. Locate the relevant feature, edition, limitation, or release note.
3. Check whether the page applies to Tencent Cloud International.
4. Record update date, edition, region, and prerequisites.

### Region availability

1. Use the Global Infrastructure page only to understand the general footprint.
2. Open the product-specific Regions, Supported Regions, Availability Zones, Purchase Guide, or API region page.
3. Confirm edition, feature, SKU, and purchase-channel restrictions.
4. Treat capacity, quota, and account eligibility as `UNKNOWN` unless directly verified.

### Pricing and billing

1. Open the product's Purchase Guide or Billing section.
2. Follow the current official Pricing Center or purchase-console link supplied by that documentation.
3. Capture currency, region, billing mode, tier, unit, effective context, and access date.
4. Separate public list price from discounts, vouchers, taxes, support, and contract terms.

Do not store static price tables in this skill.

### SLA

1. Locate the service-specific SLA under the official SLA documentation.
2. Confirm service definition, measurement unit, calculation period, exclusions, compensation, edition, and regional scope.
3. Use the general SLA only for framework context.

### Compliance

1. Start from the Compliance Center.
2. Open the exact certification or audit page.
3. Confirm service, region, legal entity, covered environment, report type, and validity period when available.
4. Avoid treating platform certification as proof of customer workload compliance.

### API and SDK

1. Open the product's API Documentation section or exact `/document/api/` page.
2. Confirm API version, action, endpoint, region parameter, request fields, response fields, rate limit, and error codes.
3. Open the product's current SDK guide for language-specific instructions.
4. Never ask a customer to paste credentials into chat.

### Troubleshooting and support

1. Check the product's troubleshooting, FAQ, error-code, monitoring, and release-note documentation.
2. Ask for sanitized error code, RequestId, timestamp, region, endpoint, SDK version, and minimal reproduction steps.
3. Use the official console ticket entry when account, quota, billing, capacity, or backend inspection is required.

## Search rules

- Restrict web research to official Tencent Cloud domains for Tencent Cloud claims.
- Use exact service names, product IDs, API actions, regions, and error codes in searches.
- Prefer the English International page for English customers and the appropriate public localized page when needed.
- Treat search snippets as navigation hints only; open the page before citing it.
- If a page is unavailable or contradictory, mark the answer `UNKNOWN` and recommend official confirmation.

## Public source boundary

Do not use private Tencent knowledge systems, internal documents, employee-only portals, unpublished decks, local customer folders, or internal messaging content. This skill must remain usable by the public without Tencent employee access.
