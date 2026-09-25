# Sales ETL Pipeline

A small, beginner-friendly **ETL (Extract, Transform, Load)** pipeline. It reads raw sales
data from a CSV file, cleans and summarises it, and loads the results into a SQLite
database — with a full automated test suite covering every stage.

This project follows the standard ETL pattern taught in most data engineering
courses (e.g. IBM's Data Engineering track): each stage is its own module, each
module has its own tests, and a single orchestrator wires them together.

## Why it's structured this way

| Stage | File | Job |
|---|---|---|
| **Extract** | `src/extract.py` | Read raw data from a source (CSV here) into a DataFrame — no cleaning, no logic. |
| **Transform** | `src/transform.py` | Clean bad/missing data, compute derived columns, aggregate for reporting. |
| **Load** | `src/load.py` | Write the result into a database (SQLite here). |
| **Orchestrator** | `src/pipeline.py` | Chains the three stages together and is the entry point you actually run. |

Splitting these up means each piece can be tested, replaced, or scaled on its own —
for example, swapping the CSV source for a live API later only touches `extract.py`.

## Project layout

```
data-engineering-pipeline/
├── src/
│   ├── extract.py       # read CSV
│   ├── transform.py     # clean + aggregate
│   ├── load.py           # write to SQLite
│   └── pipeline.py       # ties it all together, runnable script
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   ├── test_load.py
│   └── test_pipeline.py  # end-to-end integration test
├── sample_data/
│   └── sales_raw.csv     # example input with intentionally messy rows
├── requirements.txt
└── README.md
```

## Setup

```bash
cd data-engineering-pipeline
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Run the pipeline

```bash
python -m src.pipeline --csv sample_data/sales_raw.csv --db sales.db
```

This creates `sales.db` with two tables:
- **`sales_clean`** — the cleaned, row-level order data
- **`sales_by_category`** — total revenue and order count per product category

You can inspect it with the built-in `sqlite3` CLI:

```bash
sqlite3 sales.db "SELECT * FROM sales_by_category;"
```

## Run the tests

```bash
pytest -v
```

Each stage has its own unit tests (using small, hand-built DataFrames so they run
instantly with no external files needed), plus one end-to-end test in
`test_pipeline.py` that runs the whole pipeline against a temporary CSV and checks
what actually lands in the database.

## What the sample data demonstrates

`sample_data/sales_raw.csv` deliberately includes:
- A missing `customer` name → the transform stage drops that row (can't attribute a sale to nobody).
- A missing `quantity` → filled in as `1` rather than dropped, since the order itself is still valid.

This mirrors the kind of "real but slightly messy" data you'll deal with in
practice, and gives the tests something meaningful to check.

## Ideas for extending this project

- Swap the CSV extract for a public API (`requests` + JSON) or a second CSV source.
- Add a `load.py` target for PostgreSQL/MySQL instead of SQLite (same `if_exists="replace"` pattern with SQLAlchemy).
- Add data validation with [`pandera`](https://pandera.readthedocs.io/) or [`great_expectations`](https://greatexpectations.io/).
- Wrap `run_pipeline` in a scheduler (`cron`, or [Apache Airflow](https://airflow.apache.org/) once you're past the basics).
- Add a GitHub Actions workflow (`.github/workflows/tests.yml`) to run `pytest` on every push.



verification code WTC-N3VYB3SY
