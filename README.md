# AI IT Operations Toolkit

Ten bilingual Codex skills plus a safe Python toolkit and optional MCP server for incident response, technical support, infrastructure, delivery, and evidence-based portfolio work.

Diez skills bilingües para Codex, un toolkit seguro en Python y un servidor MCP opcional orientados a incidentes, soporte técnico, infraestructura, despliegues y portfolio basado en evidencia.

## Tools / Herramientas

| Tool | English | Español |
|---|---|---|
| [`incident-triage`](skills/incident-triage/README.md) | Triage impact, severity, evidence and escalation. | Evalúa impacto, severidad, evidencia y escalamiento. |
| [`log-analysis`](skills/log-analysis/README.md) | Sanitize, group and correlate logs. | Sanitiza, agrupa y correlaciona logs. |
| [`network-diagnostics`](skills/network-diagnostics/README.md) | Isolate DNS, TCP, TLS, HTTP and routing failures. | Aísla fallos de DNS, TCP, TLS, HTTP y rutas. |
| [`repository-security-audit`](skills/repository-security-audit/README.md) | Assess safe publication and repository risk. | Evalúa publicación segura y riesgos del repositorio. |
| [`server-health`](skills/server-health/README.md) | Interpret host metrics and service health. | Interpreta métricas y salud de servicios. |
| [`game-server-ops`](skills/game-server-ops/README.md) | Troubleshoot game services and player impact. | Diagnostica servicios de juegos e impacto a jugadores. |
| [`legacy-code-modernizer`](skills/legacy-code-modernizer/README.md) | Plan incremental legacy modernization. | Planifica modernización incremental de sistemas legacy. |
| [`technical-support-ticket`](skills/technical-support-ticket/README.md) | Create sanitized ticket and escalation drafts. | Crea borradores sanitizados de tickets y escalamientos. |
| [`deployment-readiness`](skills/deployment-readiness/README.md) | Produce evidence-based go/no-go decisions. | Produce decisiones go/no-go basadas en evidencia. |
| [`portfolio-evidence`](skills/portfolio-evidence/README.md) | Build honest professional claims from artifacts. | Construye afirmaciones profesionales honestas desde evidencia. |

## English

### Use as Codex skills

Copy one or more folders from `skills/` into your Codex skills directory. Each `SKILL.md` is intentionally concise and preserves authorization boundaries: diagnosis is read-only by default, while production mutations and external publication remain explicit user decisions.

### Use the local toolkit

```bash
python -m pip install -e .
ai-it-ops incident-triage --input '{"impact":"high","urgency":"high"}'
```

Every command emits JSON and reports `mutations_performed: false`.

### Run as an MCP server

```bash
python -m pip install -e ".[mcp]"
ai-it-ops-mcp
```

The MCP transport exposes the same ten deterministic, read-only assessment functions. Consumers remain responsible for confirmations and for any real infrastructure, repository, ticketing, or messaging action.

## Español

### Usar como skills de Codex

Copiá una o más carpetas de `skills/` al directorio de skills de Codex. Cada `SKILL.md` es intencionalmente breve y conserva los límites de autorización: el diagnóstico es de solo lectura por defecto, mientras que cambios productivos y publicaciones externas siguen siendo decisiones explícitas del usuario.

### Usar el toolkit local

```bash
python -m pip install -e .
ai-it-ops incident-triage --input '{"impact":"high","urgency":"high"}'
```

Cada comando entrega JSON e informa `mutations_performed: false`.

### Ejecutar como servidor MCP

```bash
python -m pip install -e ".[mcp]"
ai-it-ops-mcp
```

El transporte MCP expone las mismas diez funciones deterministas y de solo lectura. El consumidor sigue siendo responsable de pedir confirmación y ejecutar cualquier cambio real en infraestructura, repositorios, tickets o mensajes.

## Development / Desarrollo

```bash
python -m pip install -e ".[dev]"
pytest
ruff check .
```

Design principles / Principios: evidence before conclusions; minimum necessary data; redaction by default; no hidden mutations; honest attribution; reversible operational recommendations.

## License

MIT. See [LICENSE](LICENSE).
