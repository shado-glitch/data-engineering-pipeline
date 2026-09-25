import pandas as pd

from src.transform import clean_data, aggregate_by_category


def sample_raw_df():
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3, 4],
            "customer": ["Jane", "John", None, "Amy"],
            "category": ["Books", "Books", "Toys", "Toys"],
            "quantity": [1, None, 2, 3],
            "unit_price": [10.0, 10.0, 5.0, 5.0],
            "order_date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"],
        }
    )

def test_clean_data_drops_missing_customer():
    cleaned = clean_data(sample_raw_df())

    # the row with customer=None should be dropped
    assert cleaned["customer"].isna().sum() == 0
    assert len(cleaned) == 3

def test_clean_data_fills_missing_quantity_with_one():
    cleaned = clean_data(sample_raw_df())

    john_row = cleaned[cleaned["customer"] == "John"].iloc[0]
    assert john_row["quantity"] == 1

def test_clean_data_computes_total_price():
    cleaned = clean_data(sample_raw_df())

    jane_row = cleaned[cleaned["customer"] == "Jane"].iloc[0]
    assert jane_row["total_price"] == 10.0  # 1 * 10.0

def test_clean_data_parses_order_date():
    cleaned = clean_data(sample_raw_df())

    assert pd.api.types.is_datetime64_any_dtype(cleaned["order_date"])

def test_aggregate_by_category_sums_revenue():
    cleaned = clean_data(sample_raw_df())
    summary = aggregate_by_category(cleaned)

    toys_row = summary[summary["category"] == "Toys"].iloc[0]
    # Amy: 3 * 5.0 = 15.0 (John's Toys row was dropped for missing customer... wait, John is Books)
    assert toys_row["order_count"] == 1
    assert toys_row["total_revenue"] == 15.0