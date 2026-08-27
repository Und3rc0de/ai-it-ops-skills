---
name: server-health
description: Assess Linux or Windows server health from metrics, service status, storage, certificates, and logs. Use for authorized health checks and operational reports, not for unapproved remediation.
---

# Server Health

Build an evidence-based health assessment before recommending changes.

1. Establish host role, environment, maintenance window, and expected baseline.
2. Review CPU, memory, disk, inode, load, process, service, network, and certificate signals using the smallest read-only checks.
3. Distinguish saturation, transient spikes, capacity trends, and service-specific failure.
4. Correlate metrics with deployments, restarts, scheduled jobs, and user impact.
5. Rank findings by urgency and confidence. State missing telemetry explicitly.
6. Separate monitoring recommendations from remediation. Restarts, cleanup, scaling, configuration edits, and failover require explicit authorization.

Output `Health summary`, `Evidence`, `Risks`, `Unknowns`, `Next checks`, and `Remediation options`. Redact internal identifiers and secrets.
