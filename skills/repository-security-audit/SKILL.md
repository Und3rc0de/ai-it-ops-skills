---
name: repository-security-audit
description: Audit a source repository for exposed secrets, sensitive data, unsafe tracked artifacts, dependency and workflow risks, missing licensing, and publication readiness. Use before making a repository public, mirroring it, or presenting it in a portfolio.
---

# Repository Security Audit

Produce a read-only risk assessment before proposing cleanup.

## Workflow

1. Establish repository owner, intended visibility, upstream/fork relationship, license, collaborators, and authorization to publish.
2. Inspect tracked filenames and history for secrets, private keys, certificates, `.env` files, credentials, database dumps, personal data, internal endpoints, and production configuration. Do not print secret values.
3. Detect tracked dependencies, virtual environments, build outputs, caches, binaries, archives, large generated assets, and machine-specific files.
4. Review dependency manifests and lockfiles for reproducibility; use authoritative ecosystem audit tools only when available and appropriate.
5. Review CI workflows for untrusted pull-request execution, excessive permissions, unsafe interpolation, unpinned third-party actions, artifact exposure, and secret handling.
6. Distinguish current-tree cleanup from history cleanup. Deleting a secret from the latest commit does not invalidate it or remove it from history.
7. Rank findings by exploitability, sensitivity, exposure, and publication impact. Treat uncertain credentials as real until verified otherwise.
8. Recommend rotation first, then history rewriting, ignore rules, artifact cleanup, documentation, licensing, and branch protection as applicable.

Read [references/checklist.md](references/checklist.md) for publication gates and evidence categories.

## Safety

Do not delete files, rewrite history, rotate credentials, change visibility, publish, or push remediation without explicit authorization. Never include live secret material in reports, commits, issues, or pull requests.

## Output

Provide an executive summary, evidence table with sanitized paths, severity, required immediate actions, publication decision (`ready`, `blocked`, or `ready after remediation`), and a reversible remediation plan.
