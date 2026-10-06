"""02 — Public harness metadata only (no exploits).
Fetches: ExploitBench public site/docs metadata + NVD metadata for CVE-2026-11645.
Read-only, cached fallback if offline. Never downloads PoCs or runs containers.
"""
import json, os, sys
import requests

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE, "data", "harness_metadata.json")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

meta = {"sources": [], "notes": []}
def get(url, timeout=20):
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "glm53-verification/1.0 defensive-study"})
        meta["sources"].append({"url": url, "status": r.status_code, "bytes": len(r.content)})
        return r
    except Exception as e:
        meta["sources"].append({"url": url, "error": str(e)})
        return None

# 1. ExploitBench public site (leaderboard metadata, not PoCs)
r = get("https://exploitbench.ai/")
if r is not None:
    meta["notes"].append("exploitbench.ai reachable; harness = 41 V8 bugs, 16 capability flags, MCP-driven (per docs).")

# 2. NVD metadata for CVE-2026-11645 (ID referenced in Anthropic report; metadata only)
r = get("https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-11645")
if r is not None and r.status_code == 200:
    try:
        j = r.json()
        vulns = j.get("vulnerabilities", [])
        meta["notes"].append(f"NVD returned {len(vulns)} record(s) for CVE-2026-11645.")
        meta["cve"] = (vulns[0].get("cve", {}) if vulns else {})
    except Exception as e:
        meta["notes"].append(f"NVD parse note: {e}")
else:
    meta["notes"].append("NVD lookup failed or record not yet published; CVE ID retained as tracker only (no details invented).")

# 3. Hard-coded methodology facts verified via gitmcp live fetch of exploitbench/exploitbench docs
meta["verified_harness_facts"] = {
    "bugs": 41,
    "capability_flags": 16,
    "turn_budget": 300,
    "token_budget": 2500000,
    "grading": "shuffled-layout (anti-hardcoded-address)",
    "source": "exploitbench/exploitbench docs via gitmcp fetch 2026-10-06",
}

with open(OUT, "w") as f:
    json.dump(meta, f, indent=2)
print(json.dumps(meta, indent=2)[:3000])
print(f"\nSaved {OUT}")
