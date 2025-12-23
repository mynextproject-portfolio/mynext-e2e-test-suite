"""
Tests that always pass - for main branch.
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from main import add, subtract, multiply


def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(10, 5) == 5


def test_multiply():
    """Test multiplication function."""
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(4, 4) == 16

