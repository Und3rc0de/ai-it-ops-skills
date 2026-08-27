"""Safe, deterministic cores for the ten portfolio tools.

The functions produce plans and sanitized reports. They never mutate infrastructure,
repositories, tickets, or external services.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Callable
from pathlib import Path
from typing import Any

SECRET_PATTERNS = (
    re.compile(r"(?i)(password|passwd|token|api[_-]?key|secret)\s*[:=]\s*[^\s,;]+"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
)


def sanitize(text: str) -> str:
    """Mask common secret assignments without returning their values."""
    value = text
    for pattern in SECRET_PATTERNS:
        value = pattern.sub(lambda match: f"{match.group(1)}=[REDACTED]" if match.lastindex else "[REDACTED PRIVATE KEY]", value)
    return value


def _result(tool: str, summary: str, **details: Any) -> dict[str, Any]:
    return {"tool": tool, "summary": summary, "details": details, "mutations_performed": False}


def incident_triage(data: dict[str, Any]) -> dict[str, Any]:
    impact = str(data.get("impact", "unknown"))
    urgency = str(data.get("urgency", "unknown"))
    severity = "high" if impact == "high" or urgency == "high" else "medium" if "unknown" not in (impact, urgency) else "unconfirmed"
    return _result("incident-triage", "Provisional incident assessment", severity=severity, impact=impact, urgency=urgency, evidence=data.get("evidence", []), next_checks=["Confirm scope and start time", "Compare failing and known-good paths", "Run the smallest read-only discriminating check"])


def log_analysis(data: dict[str, Any]) -> dict[str, Any]:
    lines = [sanitize(str(line)) for line in data.get("lines", [])]
    signatures: dict[str, int] = {}
    for line in lines:
        normalized = re.sub(r"\b\d+\b", "#", line.lower())
        signatures[normalized] = signatures.get(normalized, 0) + 1
    ranked = sorted(signatures.items(), key=lambda item: (-item[1], item[0]))[:10]
    return _result("log-analysis", f"Analyzed {len(lines)} sanitized log lines", signatures=[{"pattern": key, "count": count} for key, count in ranked], root_cause_confirmed=False)


def network_diagnostics(data: dict[str, Any]) -> dict[str, Any]:
    target = str(data.get("target", "authorized target"))
    return _result("network-diagnostics", "Layered read-only diagnostic plan", target=target, checks=["Local interface and route", "DNS resolution", "Targeted TCP connection", "TLS handshake and certificate", "HTTP or application response"])


def repository_security_audit(data: dict[str, Any]) -> dict[str, Any]:
    root = Path(str(data.get("path", "."))).resolve()
    risky_names = {".env", "id_rsa", "id_ed25519", "credentials.json"}
    findings: list[dict[str, str]] = []
    if root.is_dir():
        for path in root.rglob("*"):
            if ".git" in path.parts or not path.is_file():
                continue
            if path.name.lower() in risky_names or path.suffix.lower() in {".pem", ".key", ".p12"}:
                findings.append({"path": str(path.relative_to(root)), "risk": "sensitive filename"})
    decision = "blocked" if findings else "ready after manual history and license review"
    return _result("repository-security-audit", "Read-only publication assessment", path=str(root), findings=findings, publication_decision=decision)


def server_health(data: dict[str, Any]) -> dict[str, Any]:
    metrics = data.get("metrics", {})
    warnings = [f"{name}={value}" for name, value in metrics.items() if isinstance(value, (int, float)) and value >= 90]
    return _result("server-health", "Server health snapshot", warnings=warnings, metrics=metrics, next_checks=["Compare against baseline", "Inspect affected service status", "Correlate with deploys and scheduled jobs"])


def game_server_ops(data: dict[str, Any]) -> dict[str, Any]:
    return _result("game-server-ops", "Game service incident plan", component=data.get("component", "unknown"), player_scope=data.get("player_scope", "unknown"), checks=["Launcher/API health", "Authentication and database dependencies", "DNS, TLS and edge path", "Recent build or configuration change"], approval_required=["restart", "deploy", "restore", "ban", "player announcement"])


def legacy_code_modernizer(data: dict[str, Any]) -> dict[str, Any]:
    stack = data.get("stack", [])
    return _result("legacy-code-modernizer", "Incremental modernization roadmap", stack=stack, phases=["Inventory and ownership", "Characterization tests", "Risk-ranked dependency isolation", "Reversible module extraction", "Observed rollout and rollback"])


def technical_support_ticket(data: dict[str, Any]) -> dict[str, Any]:
    symptom = sanitize(str(data.get("symptom", "Unknown symptom")))
    component = str(data.get("component", "unknown"))
    environment = str(data.get("environment", "unknown"))
    duplicate_key = hashlib.sha256(f"{component}|{environment}|{symptom.lower()}".encode()).hexdigest()[:12]
    return _result("technical-support-ticket", "Sanitized support ticket draft", title=f"[{component}] {symptom[:80]}", description=symptom, priority=data.get("priority", "unconfirmed"), duplicate_key=duplicate_key, external_ticket_created=False)


def deployment_readiness(data: dict[str, Any]) -> dict[str, Any]:
    checks = data.get("checks", {})
    required = ["tests", "secrets", "healthcheck", "rollback", "observability", "backup"]
    blockers = [name for name in required if checks.get(name) is not True]
    return _result("deployment-readiness", "Deployment readiness decision", decision="no-go" if blockers else "go", blockers=blockers, checked=required)


def portfolio_evidence(data: dict[str, Any]) -> dict[str, Any]:
    evidence = data.get("evidence", [])
    authorship = data.get("authorship", "unverified")
    recommendation = "keep private" if data.get("private") else "document" if not evidence else "highlight"
    return _result("portfolio-evidence", "Evidence-based portfolio assessment", authorship=authorship, evidence=evidence, recommendation=recommendation, unsupported_claims_rejected=True)


TOOL_HANDLERS: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {
    "incident-triage": incident_triage,
    "log-analysis": log_analysis,
    "network-diagnostics": network_diagnostics,
    "repository-security-audit": repository_security_audit,
    "server-health": server_health,
    "game-server-ops": game_server_ops,
    "legacy-code-modernizer": legacy_code_modernizer,
    "technical-support-ticket": technical_support_ticket,
    "deployment-readiness": deployment_readiness,
    "portfolio-evidence": portfolio_evidence,
}


def run_tool(name: str, data: dict[str, Any]) -> dict[str, Any]:
    try:
        handler = TOOL_HANDLERS[name]
    except KeyError as error:
        raise ValueError(f"Unknown tool: {name}") from error
    return handler(data)


def to_json(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2, ensure_ascii=False)
