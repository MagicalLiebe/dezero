"""Tests for DeZero."""

from dezero import __version__


def test_version() -> None:
    """Check package version."""
    assert __version__ == "0.1.0"
