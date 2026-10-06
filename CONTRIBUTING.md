# Contributing

Issues and PRs welcome. For major changes, open an issue first.

- Defensive-only contributions only — no exploits, bypasses, targets, or weight edits.
- Every number needs a source: add a row to `data/claims.csv` (metric, numerator, denominator, source, URL, access date) before touching figures or prose.
- Regenerate evidence before submitting:
  ```bash
  python experiments/01_claims_triangulation.py
  python experiments/02_public_harness_metadata.py
  python experiments/03_refusal_meta.py
  python experiments/04_hidden_patterns.py
  ```
- Test `preview.html` locally (`python -m http.server 8000`) and attach a screenshot for UI changes.
- Keep the README scannable: CEO summary first, beginner guide second, paper draft after.
