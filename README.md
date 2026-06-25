# Data Validation & Testing Framework

A pytest-based testing suite for validating data transformation logic — built to ensure analytics functions behave correctly across normal, edge, and error cases.

This is the foundation of reliable analytics: if your transformation functions silently produce wrong outputs, every dashboard and decision built on them is wrong too.

---

## What it tests

- **`apply_discount`** — percentage discount calculation with input validation
  - Normal cases: valid price and discount inputs
  - Edge cases: 0 price, 100% discount, boundary values
  - Error cases: negative prices, invalid types → raises `ValueError`

- **`is_strong_password`** — password strength validation rules
  - Normal cases: passwords meeting all criteria
  - Edge cases: borderline length, missing one rule
  - Error cases: empty string, non-string inputs

---

## Tech stack

- Python 3.13
- pytest 9.x
- conftest.py fixtures for shared test setup

---

## Run tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

---

## Structure
