# Threat Model (Defender View)

**Attacker capabilities (assumed available now):** GLM-5.3-class open weights with ~12% end-to-end V8 success per attempt, 4% full-hijack on OSS-Fuzz samples, N-day chaining at ~$20/chain, and ~0% effective refusal post-download (abliterated forks public within days).

**Attacker constraints:** 12% ≠ 100%; full chains still need iteration + infrastructure; weaponization observed in only ~1% of AI-attributed vulns (Jun 2026). Selective, not automatic.

**Defender bottleneck:** triage → patch → deploy. 0.8–6% fixed rates; maintainers capacity-constrained; NVD degraded; disclosure→exploit in hours vs 90-day disclosure norm.

**What survives missed patches (do these first):** MFA everywhere, hardened defaults, least privilege (esp. for AI tooling with broad SaaS/cloud scopes), comprehensive logging/detection, private maintainer channels pre-CVE, emergency (not quarterly) patch SLAs for browser/driver/network-device + the 97 confirmed remediations.

**What not to do:** deploy AI agents with kingdom-keys; trust model self-scored severity (recalibrate: −40pp); treat quarterly patching as sufficient.

Out of scope: offensive TTPs, target lists, exploit code. See ETHICS.md.
