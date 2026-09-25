"""
Transform stage
---------------
Cleans raw data and derives the fields the business actually needs.
Two responsibilities are split into two functions on purpose: cleaning
(fixing/removing bad rows) and aggregation (summarising for reporting)
are different jobs and are easier to test separately.
"""

import pandas as pd