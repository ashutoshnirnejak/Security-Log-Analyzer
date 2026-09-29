# statement.md

## Problem Statement
Manual security log analysis is slow and prone to errors. Repeated authentication failures (`401 Unauthorized`, `403 Forbidden`) often signal brute-force attacks, requiring automated detection to help administrators identify and mitigate risks quickly.

## Scope of the Project
A lightweight Python CLI tool that parses security logs, tracks failed logins, and flags high-risk IP addresses.

* **In-Scope:** Log parsing (`date`, `time`, `IP`, `status`), tracking `401`/`403` codes, recording first/last failure timestamps, flagging IPs exceeding `THRESHOLD = 5`, and terminal reporting.
* **Out-of-Scope:** Non-space-delimited formats (JSON/XML), automated network blocking (firewalls), real-time streaming, or GUIs.

## Target Users
* **System Administrators:** Inspecting local access logs for unauthorized attempts.
* **Cybersecurity Analysts:** Identifying brute-force activity during preliminary investigation.
* **DevOps Engineers:** Verifying authentication integrity on servers.

## High-Level Features
1. **Flexible Input Handling:** Accepts CLI args, user prompts, or falls back to a default sample file.
2. **Log Parsing & Extraction:** Discards malformed lines and isolates key fields (`date`, `time`, `IP`, `status`).
3. **Failure & Timestamp Tracking:** Maps failed login counts and captures `first_seen` and `last_seen` timestamps per IP.
4. **Threat Detection & Reporting:** Isolates IPs with failure counts above the threshold and prints a formatted terminal summary report.