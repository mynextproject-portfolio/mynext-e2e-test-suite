"""
Tests that intentionally fail - enabled on failing-tests branch.
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import add, subtract, multiply


def test_intentional_failure_add():
    """This test intentionally fails."""
    assert add(2, 2) == 5  # Wrong expected value


def test_intentional_failure_subtract():
    """This test intentionally fails."""
    assert subtract(10, 3) == 10  # Wrong expected value


def test_intentional_failure_multiply():
    """This test intentionally fails."""
    assert multiply(3, 3) == 12  # Wrong expected value

