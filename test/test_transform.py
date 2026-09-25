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
