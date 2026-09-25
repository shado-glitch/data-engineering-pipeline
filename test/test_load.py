import pandas as pd

from src.load import load_to_sqlite, read_table


def test_load_to_sqlite_roundtrip(tmp_path):
    db_path = str(tmp_path / "test.db")
    df = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"]})

    load_to_sqlite(df, db_path, "my_table")
    result = read_table(db_path, "my_table")

    assert len(result) == 3
    assert list(result["b"]) == ["x", "y", "z"]


def test_load_to_sqlite_replaces_existing_table(tmp_path):
    db_path = str(tmp_path / "test.db")
    first = pd.DataFrame({"a": [1, 2]})
    second = pd.DataFrame({"a": [9]})

    load_to_sqlite(first, db_path, "my_table")
    load_to_sqlite(second, db_path, "my_table")
    result = read_table(db_path, "my_table")

    assert len(result) == 1
    assert result["a"].iloc[0] == 9