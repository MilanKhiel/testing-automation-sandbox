# testing-automation-sandbox

Small Python project to practice writing testable code and automated tests with pytest.

## What it does

- Implements utility functions to:
  - Apply percentage discounts with input validation (`apply_discount`).
  - Check basic password strength rules (`is_strong_password`).
- Includes pytest test cases covering:
  - Normal scenarios.
  - Edge cases (0 price, 100% discount, borderline passwords).
  - Error cases (invalid inputs raising `ValueError`).

## How to run tests

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest

undefined
