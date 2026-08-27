---
name: deployment-readiness
description: Evaluate whether an application or repository is ready for deployment by checking configuration, containers, migrations, health checks, observability, backups, CI/CD, security, and rollback evidence.
---

# Deployment Readiness

Produce a deployment decision grounded in repository and environment evidence.

1. Identify target environment, release artifact, owner, dependencies, data changes, and acceptable downtime.
2. Check reproducible builds, pinned dependencies, externalized configuration, secret handling, migrations, health checks, and startup behavior.
3. Review tests, CI permissions, artifact provenance, deployment gates, observability, alerts, backups, and rollback instructions.
4. Distinguish blocking issues from improvements that can follow the release.
5. Require explicit authorization before deploying, migrating data, changing infrastructure, or rolling back.

Output a scored checklist, blockers, accepted risks, evidence links, go/no-go recommendation, deployment steps, validation checks, and rollback triggers.
