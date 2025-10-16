#!/bin/bash
# Helper script to create a commit that causes a failing test (for demo)
set -e
echo "from src.hello import greet" > tests/test_fail.py
echo "def test_fail(): assert greet('x') == 'Goodbye, x!'" >> tests/test_fail.py
git add tests/test_fail.py
git commit -m "Demonstrate failing test"
echo "Created tests/test_fail.py - push this branch to trigger a failing workflow."
