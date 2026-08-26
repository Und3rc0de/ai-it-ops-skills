---
name: log-analysis
description: Analyze application, web-server, Linux, Windows, container, and database logs to identify patterns, correlate events, test hypotheses, and produce a privacy-conscious diagnostic summary. Use for troubleshooting and incident investigation, not indiscriminate log collection.
---

# Log Analysis

Analyze the minimum relevant log window and preserve the distinction between correlation and causation.

## Workflow

1. Confirm source, environment, timezone, time window, expected behavior, and the symptom being investigated.
2. Normalize timestamps only when needed; retain the original value alongside conversions used in the analysis.
3. Remove or mask secrets and personal data before quoting or exporting evidence.
4. Establish a baseline, then group repeated events by signature rather than counting raw lines alone.
5. Correlate request IDs, trace IDs, process IDs, hosts, users, endpoints, deployments, or restarts when those fields exist.
6. Test at least one alternative explanation for each leading hypothesis.
7. Distinguish the trigger, contributing conditions, user-visible consequence, and confirmed root cause.
8. Recommend targeted follow-up queries or checks; avoid broad collection when a narrower check can answer the question.

Read [references/patterns.md](references/patterns.md) when selecting fields or interpreting common web, application, authentication, resource, and database signals.

## Output

Report the analyzed scope, strongest findings, representative sanitized examples, confidence, competing explanations, missing evidence, and next checks. Never claim a root cause from temporal proximity alone.
