"""
Extract stage
-------------
Responsible for ONE thing: pulling raw data from a source (here, a CSV
file) into a pandas DataFrame, with no cleaning or business logic.

Keeping extract/transform/load in separate modules is the classic ETL
pattern: each stage can be tested, replaced, or scaled independently
(e.g. swap this CSV read for a database query or an API call later
without touching transform.py or load.py).
"""

import pandas as pd

def extract_data(csv_path: str) -> pd.DataFrame:
    """
    Read a CSV file of raw sales records into a DataFrame.

    Parameters
    ----------
    csv_path : str
        Path to the source CSV file.

    Returns
    -------
    pd.DataFrame
        Raw, unvalidated data exactly as it appears in the source.

    Raises
    ------
    FileNotFoundError
        If csv_path does not exist.
    """
    df = pd.read_csv(csv_path)
    return df