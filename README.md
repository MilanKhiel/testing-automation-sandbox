# Testing & Automation Sandbox (Python, pytest)

This project implements functions to apply price discounts and check password strength with clear input validation and error handling. It also includes pytest tests that cover normal, edge, and invalid cases to automatically verify that the behavior is correct.

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
