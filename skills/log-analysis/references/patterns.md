# Diagnostic patterns

## Useful correlation fields

Prefer request/trace ID, timestamp, host, service, environment, version, endpoint, status code, duration, process ID, user or tenant identifier, and upstream dependency. Redact identifiers when they are unnecessary for the conclusion.

## Common signals

- Web/API: shifts in 4xx/5xx rate, latency percentiles, timeouts, retry storms, payload-size errors, and one endpoint or upstream dominating failures.
- Authentication: clock skew, token expiry, issuer/audience mismatch, key rotation, authorization denial, and session-store failure.
- Resources: memory pressure, out-of-memory termination, disk-full errors, file-descriptor exhaustion, CPU saturation, and connection-pool exhaustion.
- Database: lock waits, deadlocks, slow queries, connection limits, migration mismatch, replica lag, and transaction rollback.
- Deployments: first occurrence after a release, configuration drift, schema mismatch, missing environment values, or incompatible dependency versions.

An exception message identifies where a failure surfaced, not necessarily where it originated.
