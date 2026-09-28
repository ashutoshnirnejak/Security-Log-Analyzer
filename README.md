# Log Analyzer

A small command-line tool that scans a security log file for repeated
failed login attempts (HTTP `401` / `403` status codes) and flags any
IP address whose failure count goes above a configurable threshold.

## Project structure

```
log_analyzer_project/
├── run.py                          # Entry point - run this file
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│   └── log_analyzer/
│       ├── __init__.py
│       ├── config.py                # Constants (failure codes, threshold)
│       ├── file_reader.py           # Reads the log file, handles I/O errors
│       ├── log_parser.py            # Turns raw lines into LogEntry objects
│       ├── failure_tracker.py       # Counts failures per IP + timestamps
│       ├── suspicious_detector.py   # Applies the "above threshold" rule
│       ├── report_generator.py      # Builds and prints the report
│       ├── input_handler.py         # Decides which file to analyze
│       ├── main.py                  # Wires all modules together
│       └── sample_security_log.txt  # Sample data, used by default
└── tests/
    ├── __init__.py
    ├── test_file_reader.py
    ├── test_log_parser.py
    ├── test_failure_tracker.py
    ├── test_input_handler.py
    ├── test_suspicious_detector.py
    └── test_report_generator.py
```

Each module has a single responsibility (read, parse, track, detect,
report, or decide input), which keeps the code easy to follow, test,
and extend on its own.

## Requirements

Python 3.8+. No external runtime libraries are required — the project
only uses the standard library. `pytest` is listed as an optional
dev dependency for running tests, but the built-in `unittest` runner
works too (see below).

## Running it

From the project root:

```bash
python run.py
```

This will ask you for a log file path. Press **Enter** to use the
bundled sample file instead.

You can also pass a file directly, skipping the prompt:

```bash
python run.py path/to/your_log.txt
```

A typed filename is looked for as given, then next to the program
files. If it still can't be found, the program prints a warning and
falls back to the bundled sample file automatically.

## Log file format

Each line is expected to look like:

```
<date> <time> <ip_address> <status_code>
2026-09-27 09:01:05 192.168.1.12 401 Login failed
```

Only the first four fields are used; any extra text (like the message)
is ignored. Lines with fewer than 4 fields are skipped rather than crashing the
program.

## Running the tests

Using the standard library (no installation needed):

```bash
python -m unittest discover -s tests -v
```

Or, if you have `pytest` installed:

```bash
pytest
```

## Design Notes

- **Separation of concerns**: reading, parsing, tracking, detecting,
  and reporting are each their own module, so a change to one (e.g.
  how a report is formatted) can't accidentally break another (e.g.
  how failures are counted).
- **Error handling**: `file_reader.py` catches missing files,
  permission errors, and invalid text instead of letting the whole
  program crash; `log_parser.py` skips malformed lines instead of
  raising exceptions.
- **Testability**: functions take plain data in and return plain data
  out wherever possible (e.g. `build_report` returns a string instead
  of printing directly), which is what makes them easy to unit test.

  **Project Screenshots**

  # Starting Interface
<img width="1917" height="1018" alt="Screenshot 2026-09-29 000501" src="https://github.com/user-attachments/assets/ef812e48-db9f-4c20-95ee-ef9a02dcaa63" />
