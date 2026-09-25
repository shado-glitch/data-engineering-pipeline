import pandas as pd
import pytest

from src.extract import extract_data


def test_extract_reads_all_rows(tmp_path):
    csv_file = tmp_path / "orders.csv"
    csv_file.write_text(
        "order_id,customer,category,quantity,unit_price,order_date\n"
        "1,Jane,Books,1,10.0,2026-01-01\n"
        "2,John,Books,2,10.0,2026-01-02\n"
    )

    df = extract_data(str(csv_file))

    assert len(df) == 2
    assert list(df.columns) == [
        "order_id",
        "customer",
        "category",
        "quantity",
        "unit_price",
        "order_date",
    ]
