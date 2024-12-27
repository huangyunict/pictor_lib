"""Test module for the class PictorSize."""
import configparser
import json
from pathlib import Path

from src.pictor_lib.pictor_size import PictorSize


class TestPictorSize:
    """Tests for the class PictorSize."""

    def test_new_size_with_defaults(self):
        """Test for creating a new object with defaults."""

        size = PictorSize()

        # Verify size.
        assert size.width == 0
        assert size.height == 0

    def test_new_size_with_values(self):
        """Test for creating a new object with values."""

        size = PictorSize(width=800, height=600)

        # Verify size.
        assert size.width == 800
        assert size.height == 600
