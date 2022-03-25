#!/bin/sh
pylint transactions.py
pylint tracker.py
pytest -v test_transactions.py