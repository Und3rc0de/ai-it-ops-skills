---
name: network-diagnostics
description: Diagnose connectivity, DNS, routing, ports, HTTP, TLS, proxy, firewall, and service-reachability problems using layered, minimally invasive checks. Use for troubleshooting authorized systems; do not use for scanning unrelated networks or bypassing access controls.
---

# Network Diagnostics

Locate the failing layer before recommending configuration changes.

## Workflow

1. Define source, destination, expected protocol/port, environment, time of failure, and whether the issue affects one client, one network, or all consumers.
2. Confirm local interface, address, route, proxy/VPN context, and name resolution before testing the application.
3. Test progressively: DNS result, route/reachability, TCP connection, TLS handshake, HTTP/application response, then dependency-specific behavior.
4. Compare a failing path with a known-good path when available. Record both negative and positive evidence.
5. Account for split DNS, IPv4/IPv6 differences, NAT, load balancers, proxies, CDN/WAF behavior, certificates, SNI, redirects, and asymmetric firewall rules.
6. Prefer targeted checks against user-authorized hosts and ports. Do not perform subnet sweeps, broad port scans, credential attacks, evasion, or persistence.
7. Separate a proposed fix from diagnosis. Changes to DNS, routes, firewall rules, certificates, VPNs, proxies, or production services require explicit authorization and a rollback plan.

Read [references/layers.md](references/layers.md) for a compact decision guide.

## Output

State the failing layer, evidence, confidence, affected path, plausible alternatives, and the next smallest check. Include sanitized commands only when they help the user reproduce the result.
