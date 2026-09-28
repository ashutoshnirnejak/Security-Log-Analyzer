"""
run.py

Convenience entry point at the project root.

Usage:
    python run.py                     # prompts for a file, or uses the sample
    python run.py path/to/mylog.txt   # analyzes the given file directly
"""

from src.log_analyzer.main import run

if __name__ == "__main__":
    run()
