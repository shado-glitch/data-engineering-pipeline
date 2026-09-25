"""
Pipeline orchestrator
----------------------
Wires the three stages together. This is the only module that knows
about the full sequence -- extract, transform, load -- so it's the
single place to look to understand "what does this pipeline actually
do end to end".
"""

import argparse

from src.extract import extract_data
from src.transform import clean_data, aggregate_by_category
from src.load import load_to_sqlite



def run_pipeline(csv_path: str, db_path: str) -> None:
    """
    Run the full ETL pipeline: extract raw CSV -> clean -> aggregate
    -> load both the cleaned records and the category summary into
    SQLite.
    """
    raw = extract_data(csv_path)
    cleaned = clean_data(raw)
    summary = aggregate_by_category(cleaned)

    load_to_sqlite(cleaned, db_path, "sales_clean")
    load_to_sqlite(summary, db_path, "sales_by_category")

    print(f"Loaded {len(cleaned)} cleaned orders into {db_path} (table: sales_clean)")
    print(f"Loaded {len(summary)} category rows into {db_path} (table: sales_by_category)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the sales ETL pipeline.")
    parser.add_argument("--csv", default="sample_data/sales_raw.csv", help="Path to source CSV")
    parser.add_argument("--db", default="sales.db", help="Path to output SQLite database")
    args = parser.parse_args()

    run_pipeline(args.csv, args.db)
