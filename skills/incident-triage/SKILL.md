---
name: incident-triage
description: Triage IT and application incidents from symptoms, alerts, tickets, or user reports. Use when the goal is to establish impact, urgency, evidence, likely fault domain, safe next checks, and an escalation-ready incident summary.
---

# Incident Triage

Turn incomplete reports into an evidence-based incident record and a safe investigation plan.

## Workflow

1. Separate observed facts from assumptions and unverified reports.
2. Establish scope: affected users, systems, environments, regions, start time, recurrence, and business impact.
3. Assign a provisional severity using impact and urgency. State the local severity convention when one is provided; otherwise explain the chosen level without pretending it is universal.
4. Build a short timeline in one timezone and preserve original timestamps when conversion matters.
5. Classify the likely fault domain: client, identity, network, DNS/TLS, application, dependency, database, infrastructure, deployment, or unknown.
6. Propose the smallest read-only checks that can discriminate between competing hypotheses. Prioritize checks with high information value and low production risk.
7. Identify containment options separately from root-cause investigation. Never execute restarts, failovers, rollbacks, blocking rules, or data changes without explicit authorization.
8. Produce an escalation-ready summary with evidence, uncertainty, completed checks, current impact, next owner, and recommended next action.

## Output

Use concise sections: `Current status`, `Impact`, `Timeline`, `Evidence`, `Working hypotheses`, `Next checks`, `Containment options`, and `Escalation notes`. Mark unknown fields explicitly rather than filling them with guesses.

Treat credentials, tokens, personal data, internal hostnames, and customer content as sensitive. Redact them from summaries unless the user explicitly requires and authorizes their inclusion.
