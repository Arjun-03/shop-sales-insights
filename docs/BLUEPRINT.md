# Shop Sales Insights — Technical Blueprint (v1)

Status: agreed in Phase 0 (14 Oct 2026). Changes to this document require an explicit decision.

## 1. Purpose

A local, single-user application for one grocery shop in Sri Lanka to:

- record bills (total amount only, no line items),
- manage customers (with a shared Walk-in Customer for anonymous sales),
- correct bills with a full audit trail,
- analyse sales and customer behaviour,
- export to Excel and back up / restore the database safely.

Digital records start from the launch date. No historical migration.

## 2. Scope

### In scope (v1)
- Bill management: auto bill number, manual purchase date, customer, total (LKR), payment method (cash initially), created/updated timestamps, voiding, audited corrections.
- Customer management: auto ID, name, optional phone, duplicate-phone warning, purchase history and lifetime metrics.
- Sales dashboard: totals, bill count, average bill value, daily/weekly/monthly trends, date filters.
- Customer analytics: new vs repeat, top customers, purchase histories, inactive customers with configurable threshold.
- Excel exports, manual backup, verified restore.

### Out of scope (v1)
Inventory, product/category analytics, profit/cost, barcode scanning, receipt printing, multiple branches or users, cloud hosting, automated promotions or messaging, login.

## 3. Technology stack

| Component | Role |
|-----------|------|
| Python 3.13 | Language for all logic |
| Streamlit | Local web UI and dashboards |
| SQLite | Single-file relational database |
| SQL | Storing and querying records |
| Pandas | Aggregations for analytics and exports |
| Plotly | Interactive charts |
| OpenPyXL | Excel (.xlsx) writing engine |
| pytest | Automated tests |
| Git + GitHub | Version control (public repo, code only) |

Exact library versions are pinned in `requirements.txt` at install time.

## 4. Architecture (layers)

```
Streamlit UI (pages/)            -> displays forms, tables, charts; no SQL, no calculations
   |
Business logic (shop_insights/)  -> validation, rules, analytics, exports, backup
   |
Data access (shop_insights/db.py)-> connections, transactions, parameterized SQL
   |
SQLite file (data/shop.db)
```

Rules:
- The UI calls business-logic functions only.
- Every SQL statement uses parameters (never string formatting).
- Calculations live outside the UI so they can be tested with pytest.

## 5. Folder structure

```
shop-sales-insights/
├── app.py
├── pages/
├── shop_insights/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│   ├── schema.sql
│   ├── money.py
│   ├── validation.py
│   ├── customers.py
│   ├── bills.py
│   ├── analytics.py
│   ├── charts.py
│   ├── exports.py
│   └── backup.py
├── tests/
├── docs/
├── data/        (git-ignored)
├── backups/     (git-ignored)
├── exports/     (git-ignored)
├── requirements.txt
├── .gitignore
└── README.md
```

Files are created only when the milestone that needs them begins.

## 6. Agreed design decisions

| ID | Decision |
|----|----------|
| D1 | Money is stored as **integer cents** (Rs 1,250.50 -> 125050). User input is parsed with `Decimal`, never `float`. Bills include cents. |
| D2 | Bill identity is the database's auto-increment ID, displayed as `B-000001`. |
| D3 | Bills are never hard-deleted. Incorrect bills are **voided** with a reason. Void bills are excluded from totals but remain visible and audited. |
| D4 | Sri Lankan phone numbers are normalized before storage/comparison (e.g. `077 123 4567`, `0771234567`, `+94771234567` -> `+94771234567`). |
| D5 | Weeks start Monday (ISO). Dates use local time (Asia/Colombo). Future purchase dates are rejected; dates before launch produce a warning. |
| D6 | "New" customer in a period = first recorded bill falls in the period. "Repeat" = had a bill before the period and buys again within it. Walk-in excluded from both. A first *recorded* purchase may not be the first-ever visit. |
| D7 | Public GitHub repo containing **code only**. The database, backups, exports and any real customer data are never committed. Sample/test data is fictional. |

## 7. Data model (preview — finalized in Phase 2)

- `customers` — id, name, phone (nullable, normalized), is_walk_in, created_at, updated_at
- `bills` — id, customer_id (FK -> customers), purchase_date, amount_cents, payment_method, status (active/void), created_at, updated_at
- `bill_audit` — id, bill_id (FK -> bills), action, old values, new values, reason, changed_at

## 8. Risks and mitigations

| Risk | Mitigation |
|------|-----------|
| Computer failure loses all data | Manual backups to an external/USB drive; tested restore procedure |
| No login: anyone at the computer can view data | Password-protect the Windows user account; document the limitation |
| Data-entry errors (extra zero, wrong date) | Validation, confirmation for unusually large amounts, audited corrections |
| Customer data leaking to public GitHub | `.gitignore` from the first commit; data folders outside version control; review `git status` before every commit |
| Floating-point rounding errors | Integer cents + `Decimal` parsing |
| Library updates breaking the app | Pinned versions; update deliberately and re-run tests |

## 9. Release-readiness (v1)

The app is ready for business use only after the Phase 8 checklist (tests passing, backup restored successfully on a separate copy, maintenance guide understood) is completed.
