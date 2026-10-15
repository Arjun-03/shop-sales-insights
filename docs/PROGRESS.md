# Progress Log

## Completed
- [x] Phase 0 — Requirements confirmed, architecture and design decisions D1–D7 agreed (14 Oct 2026)
- [x] Phase 1 — Development environment and foundations (15 Oct 2026)
  - [x] 1.1 Python 3.13.16 installed alongside 3.12; verified with the `py` launcher
  - [x] 1.2 Terminal basics; project folder at C:\Users\arjun\personal-projects\shop-sales-insights; VS Code
  - [x] 1.3 Virtual environment (.venv on Python 3.13)
  - [x] 1.4 Dependencies installed and pinned in requirements.txt; import smoke test passed
  - [x] 1.5 Git initialised; .gitignore committed first; pushed to public GitHub repo with noreply email
  - [x] 1.6 Minimal Streamlit app (app.py) running locally; .streamlit/config.toml restricts access to localhost and disables usage stats

## Next
- [ ] Phase 2 — Database and SQL

## Remaining
- [ ] Phase 3 — Customer and bill management
- [ ] Phase 4 — Sales dashboard
- [ ] Phase 5 — Customer analytics
- [ ] Phase 6 — Excel exports, backups, auditability
- [ ] Phase 7 — Testing and quality
- [ ] Phase 8 — Final setup and maintenance

## Known issues
- Only direct dependencies are pinned in requirements.txt; transitive dependencies may drift on a rebuild. Revisit full locking in Phase 8.

## Notes
- Pinned versions (14 Oct 2026): streamlit 1.65.0, pandas 3.0.6, plotly 7.1.0, openpyxl 3.1.5, pytest 9.1.1, tzdata 2026.5.
- pandas 3.x: many online tutorials target pandas 1.x/2.x; check examples against the pandas 3 docs.
- Before every commit: run `git status` and read the staged list.