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
