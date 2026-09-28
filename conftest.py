"""
conftest.py

Makes sure the project root is on sys.path so tests can import
`src.log_analyzer...` regardless of which directory pytest is run
from.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
