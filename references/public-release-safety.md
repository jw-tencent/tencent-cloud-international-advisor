# Public Release Safety

Apply this checklist before publishing the skill, examples, issues, pull requests, screenshots, or generated deliverables.

## Do not publish

- API keys, tokens, passwords, certificates, private keys, cookies, or session data.
- Customer names, personal information, account identifiers, contracts, invoices, or negotiated pricing without explicit authorization.
- Public IP addresses, internal domains, hostnames, topology details, logs, tickets, or screenshots that identify a real environment.
- Private roadmap items, unreleased capabilities, internal product codenames, escalation paths, internal contacts, or internal knowledge-base references.
- Local filesystem paths that reveal a person's name, employer, customer, or project structure.
- Proprietary slide text, diagrams, licensed reports, or copyrighted material without redistribution permission.
- Unsupported benchmark, market-share, savings, payback, performance, or superiority claims.

## Safe alternatives

- Replace real customers with clearly fictional names.
- Replace real identifiers with obvious placeholders such as `[CUSTOMER]`, `[REGION]`, and `[ACCOUNT_ID]`.
- Use documentation links that are already publicly accessible.
- Convert specific commercial values into blank templates or transparent sample assumptions.
- Label fictional data and estimated values explicitly.
- Reproduce a workflow or method in original language instead of copying internal documentation.

## Review procedure

1. Search all files, including hidden files and history, for secrets and sensitive identifiers.
2. Review every URL and remove internal or access-controlled domains.
3. Review every named company and person; keep only public vendors or clearly fictional examples.
4. Review every number; add a source, mark it as an estimate, or remove it.
5. Review metadata, comments, screenshots, archives, and generated artifacts.
6. Confirm the license permits distribution of every included file.
7. Perform a final human review before changing a repository from private to public.

## Evidence rule for public examples

Public examples may demonstrate the structure of a comparison or TCO model, but must not imply that placeholder data is a verified customer result. Use `ESTIMATE` and `FICTIONAL EXAMPLE` labels prominently.
