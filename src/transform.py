"""
Transform stage
---------------
Cleans raw data and derives the fields the business actually needs.
Two responsibilities are split into two functions on purpose: cleaning
(fixing/removing bad rows) and aggregation (summarising for reporting)
are different jobs and are easier to test separately.
"""

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw sales data:
    - Drop rows with a missing customer name (can't attribute the sale).
    - Fill missing quantity with 1 (treat as a single-item order).
    - Compute a `total_price` column (quantity * unit_price).
    - Parse `order_date` into a real datetime.

    Parameters
    ----------
    df : pd.DataFrame
        Raw data as returned by extract_data().

    Returns
    -------
    pd.DataFrame
        Cleaned data, ready for aggregation or loading.
    """
    clean = df.copy()

    clean = clean.dropna(subset=["customer"])
    clean["quantity"] = clean["quantity"].fillna(1)
    clean["quantity"] = clean["quantity"].astype(int)
    clean["unit_price"] = clean["unit_price"].astype(float)
    clean["total_price"] = clean["quantity"] * clean["unit_price"]
    clean["order_date"] = pd.to_datetime(clean["order_date"])

    return clean.reset_index(drop=True)