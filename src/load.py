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