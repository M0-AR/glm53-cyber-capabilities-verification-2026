# Reproducibility (2026–2027 Best Practice)

1. **Claims ledger first:** `data/claims.csv` — every number has source URL + access date. No number enters a figure without a ledger row.
2. **Sequential search:** one websearch at a time (no parallel → no 429); backoff 5s → 10s ×3; fallback DuckDuckGo lite HTML; then MCP tools (SearXNG, OpenResearch, paper-search, DuckDuckGo, agent-reach, gitmcp, Kaggle, wiki, GSD). Different keywords per tool (voting across opinions).
3. **Pinned environment:** `Dockerfile` (python:3.11-slim) + `requirements.txt` + `docker-compose.yml`. Run: `docker compose up --build`, open `http://localhost:8888` (token `glm53`).
4. **Deterministic analysis:** `experiments/0X_*.py` in order; matplotlib `Agg`; Wilson CIs; figures to `figures/`. No network required except `02_*` (cached fallback).
5. **No benchmark pollution:** per ExploitBench request, no RL training on benchmark envs; read-only public snapshots only; digest-pin any image before citing.
6. **Auditability:** keep transcripts/tool logs for any future live work (SHA-256 manifests per ExploitBench audit-bundle pattern); timestamp ledger snapshots (counts move daily).
7. **Versioning:** tag releases `vYYYY.MM.DD-ledger-N`; never rewrite published CSV rows — append corrections.
