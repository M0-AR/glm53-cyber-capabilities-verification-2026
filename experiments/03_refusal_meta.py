"""03 — Refusal-ladder meta-analysis (published numbers only).
No prompts executed, no models run. Plots Anthropic's 0/64/92/100 vs Claude 0,
alongside literature ORTHO ASRs (Arditi et al. 2024, Table 2: Qwen 79-84%).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(BASE, "figures", "03_refusal_ladder.png")
os.makedirs(os.path.dirname(FIG), exist_ok=True)

conds = ["bare\norder", "+cover\nstory", "+prefill", "abliterated"]
glm = [0, 64, 92, 100]
claude = [0, 0, None, None]  # prefill/abliteration N/A by API/weights design

x = range(len(conds))
plt.figure(figsize=(7, 4))
plt.plot(x, glm, marker="o", label="GLM-5.3 (Anthropic sim, n=50/cell)")
plt.plot([0, 1], [0, 0], marker="s", label="Claude safeguarded (applicable cells)")
plt.xticks(list(x), conds)
plt.ylabel("% engagement (tried to connect)")
plt.title("Published safeguard ladder — simulation only, no replication")
plt.ylim(-5, 105)
plt.legend()
plt.tight_layout()
plt.savefig(FIG, dpi=150)

print("GLM ladder:", glm)
print("Claude (applicable): 0, 0; prefill/abliteration N/A by design (no thinking-prefill API; weights unreleased).")
print("Literature anchor: ORTHO HARMBENCH ASR 79.2/84.3/78.0% (Qwen 7/14/72B) vs Anthropic post-abliteration compliance 88-98% — same order.")
print(f"Saved {FIG}")
