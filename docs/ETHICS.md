# Ethics — Defensive-Only, No Live Work

1. **No red-teaming.** We do not run GLM-5.3/Flash, abliterated forks, or any model against vulnerable targets. We do not craft, test, or publish jailbreak prompts, prefill strings, cover stories, or weight-edit code.
2. **No exploit artifacts.** No PoCs, no shellcode, no ROP chains, no browser pages, no driver/firmware probes. CVE-2026-11645 appears by ID only.
3. **Simulations are not replicated.** Anthropic's harness uses a fake bash tool + LLM-approximated results. We cite its *rates* (0/64/92/100) as willingness-to-engage signals, not real-world success probabilities.
4. **Coordinated disclosure respected.** Browser/driver/device flaws are referenced at the granularity of the public reports ("disclosed to maintainer", "under review"). No version fingerprints that accelerate weaponization.
5. **Dual-use handling.** Cost figures ($20.40, ~$1,200) are published to motivate patch urgency, without instructions to achieve them. Economics, not recipes.
6. **Human data.** No human subjects. Public-figure reporting (Anthropic, CAISI, Z.ai, Vulncheck, CSA) only.
7. **Open-weight caution.** We state plainly: assume downloaded weights ≈ 0% refusal (abliterated forks appeared within days). This is a warning, not an endorsement.
8. **Review.** Any future extension touching models requires IRB/security review + coordinated-disclosure plan before code is written.

If in doubt: analyze aggregates, harden systems, disclose responsibly.
