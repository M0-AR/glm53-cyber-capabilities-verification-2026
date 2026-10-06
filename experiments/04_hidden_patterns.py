"""04 — Hidden-pattern arithmetic from published aggregates only.
Computes: cost collapse, severity calibration gap, patch-lag ratios, timeline compression.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(BASE, "figures", "04_economics.png")
os.makedirs(os.path.dirname(FIG), exist_ok=True)

print("== Cost collapse (Anthropic published) ==")
print(f"N-day chain: $20.40 for 20min human + 8h model (GLM-5.3-Flash, CVE-2026-11645 + 1 more, ARM64 PAC bypass)")
print(f"Abliteration: $4,400 first-try (2,200 GPUh) -> ~$1,200 experienced (~600 GPUh)")
print(f"Implication: marginal attacker = anyone with a credit card, not just nation-states.")

print("\n== Severity calibration gap ==")
print(f"Claude hi/crit: 91.5% vs maintainers 51.3% -> delta 40.2pp (Vulncheck/Garrity ledger audit).")
print("Implication: triage needs maintainer-calibrated scoring, not model self-scoring.")

print("\n== Patch lag ==")
print("Ledger: 26,153 findings -> 2,736 ledgered (10.5%) -> 2,096 reported (8%) -> 202 fixed (0.8%).")
print("CSA: 1,596 disclosed / 281 projects -> 97 patched (~6%).")
print("AI-attributed exploited in wild: 14/1,061 (~1.3%) as of Jun 2026.")
print("Timelines: 771 days (2018) -> single-digit hours; 28.3% CVEs <24h; CVE +263% 2020-25; NVD enrichment degraded.")

print("\n== Chain-scaling (Z.ai self-report) ==")
print("CyberGym +7.3pp (77.2->84.5) | ExploitBench +30.0pp (24.4->54.4, 2.2x) | ExploitGym 29/39 -> 105/130 (3.6x/3.3x).")
print("Pattern: gains largest further up the exploitation chain.")

labels = ["N-day chain", "Abliteration\n(first try)", "Abliteration\n(experienced)"]
costs = [20.40, 4400, 1200]
plt.figure(figsize=(7, 4))
plt.bar(labels, costs)
plt.ylabel("USD (log scale)")
plt.yscale("log")
plt.title("Attacker economics (published costs, log scale)")
for i, c in enumerate(costs):
    plt.text(i, c*1.15, f"${c:,.0f}", ha="center")
plt.tight_layout()
plt.savefig(FIG, dpi=150)
print(f"\nSaved {FIG}")
