---
name: game-server-ops
description: Operate and troubleshoot authorized online game services, launchers, APIs, player connectivity, backups, and deployments. Use for community infrastructure such as Servers-GX; require approval before player-impacting actions.
---

# Game Server Operations

Treat the game platform as a production client-server system.

1. Identify the affected game, realm, launcher/API component, region, build, and player scope.
2. Correlate player reports with service health, authentication, database, DNS/TLS, CDN/WAF, network, and deployment evidence.
3. Prefer read-only status, log, endpoint, and dependency checks.
4. Separate client, account, ISP, edge, application, database, and host hypotheses.
5. Verify backup age and restore documentation without exposing player data.
6. Require explicit authorization before restarts, bans, configuration changes, deployments, restores, or player-facing announcements.

Output current impact, timeline, evidence, likely fault domain, safe checks, recovery options, rollback criteria, and a sanitized player-support message.
