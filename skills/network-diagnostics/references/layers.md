# Layered decision guide

- Name fails to resolve: inspect resolver choice, search suffix, split DNS, record type, TTL, and authoritative answer.
- Address resolves but route fails: inspect source address, gateway, VPN, route selection, IPv4/IPv6, and upstream reachability.
- TCP fails: verify the exact destination/port, listener state, security group or firewall path, NAT, and load balancer health.
- TLS fails: inspect SNI, certificate chain, hostname, validity period, trust store, protocol/cipher compatibility, and intercepting proxy.
- HTTP responds incorrectly: inspect status, redirect chain, host header, proxy/CDN/WAF, authentication, upstream response, and application logs.
- Intermittent failure: correlate by backend, address family, region, deployment, connection reuse, timeout, packet loss, or resource saturation.

ICMP success does not prove that an application port works; ICMP failure does not prove that the service is unreachable.
