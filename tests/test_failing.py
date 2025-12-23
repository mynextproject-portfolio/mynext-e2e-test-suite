"""
Tests that can be configured to fail - skipped on main, enabled on failing-tests branch.
"""
import sys
from pathlib import Path
import pytest

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import add, subtract, multiply


@pytest.mark.skip(reason="Skipped on main branch - enable on failing-tests branch")
def test_intentional_failure_add():
    """This test intentionally fails when enabled."""
    assert add(2, 2) == 5  # Wrong expected value


@pytest.mark.skip(reason="Skipped on main branch - enable on failing-tests branch")
def test_intentional_failure_subtract():
    """This test intentionally fails when enabled."""
    assert subtract(10, 3) == 10  # Wrong expected value


@pytest.mark.skip(reason="Skipped on main branch - enable on failing-tests branch")
def test_intentional_failure_multiply():
    """This test intentionally fails when enabled."""
    assert multiply(3, 3) == 12  # Wrong expected value

