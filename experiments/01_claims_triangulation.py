"""01 — Triangulate published ExploitBench / binary-exp counts.
Defensive-only: recomputes proportions + Wilson 95% CIs from PUBLISHED aggregates.
No model runs, no exploits. Source: data/claims.csv (Anthropic 2026-09-29, CAISI 2026-09-17).
"""
import math, csv, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(BASE, "figures", "01_exploitbench.png")
os.makedirs(os.path.dirname(FIG), exist_ok=True)

def wilson(k, n, z=1.96):
    if n == 0: return (0, 0, 0)
    p = k / n
    d = 1 + z*z/n
    c = p + z*z/(2*n)
    m = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n))
    return p, max(0, (c-m)/d), min(1, (c+m)/d)

rows = [
    ("GLM-5.3", 50, 410),
    ("Mythos Preview", 56, 410),
    ("GLM-5.2", 0, 410),
    ("Opus 4.6 (approx)", 0, 410),
]
print("== ExploitBench end-to-end (Anthropic setup, 410 attempts) ==")
for name, k, n in rows:
    p, lo, hi = wilson(k, n)
    print(f"{name:18s} {k:3d}/{n} = {p*100:5.2f}%  95%CI [{lo*100:.1f}, {hi*100:.1f}]")

print("\n== Binary-exp full hijack (100 tasks) ==")
for name, k in [("GLM-5.3", 4), ("Mythos", 6), ("predecessors", 0)]:
    p, lo, hi = wilson(k, 100)
    print(f"{name:14s} {k}/100 = {p*100:.1f}%  95%CI [{lo*100:.1f}, {hi*100:.1f}]")

# Plot
labels = [r[0] for r in rows]
ps = [wilson(k, n)[0]*100 for _, k, n in rows]
los = [wilson(k, n)[1]*100 for _, k, n in rows]
his = [wilson(k, n)[2]*100 for _, k, n in rows]
yerr = [[p-lo for p, lo in zip(ps, los)], [hi-p for p, hi in zip(ps, his)]]
plt.figure(figsize=(7, 4))
plt.bar(labels, ps, yerr=yerr, capsize=4)
plt.ylabel("% end-to-end success (410 attempts)")
plt.title("ExploitBench end-to-end (published counts, Wilson 95% CI)")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.savefig(FIG, dpi=150)
print(f"\nSaved {FIG}")
print("INTERPRETATION: GLM-5.3 ~ Mythos (overlapping CIs); predecessors at 0 -> threshold crossed (existence, not ranking).")
