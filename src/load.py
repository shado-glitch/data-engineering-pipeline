"""
Load stage
----------
Writes a DataFrame into a SQLite database table. SQLite is used here
because it needs no server setup, making the whole pipeline runnable
with nothing but Python installed -- useful for a learning project or
a CI test run.
"""

import sqlite3
import pandas as pd

def load_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str) -> None:
    """
    Write a DataFrame to a SQLite table, replacing it if it exists.

    Parameters
    ----------
    df : pd.DataFrame
        Data to persist.
    db_path : str
        Path to the SQLite database file (created if it doesn't exist).
    table_name : str
        Name of the table to write to.
    """
    connection = sqlite3.connect(db_path)
    try:
        df.to_sql(table_name, connection, if_exists="replace", index=False)
        connection.commit()
    finally:
        connection.close()