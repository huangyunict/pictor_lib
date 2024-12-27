"""Test module for the class PictorSize."""
import configparser
import json
from pathlib import Path

from src.pictor_lib.pictor_size import PictorSize


class TestPictorSize:
    """Tests for the class PictorSize."""

    def test_new_manager_with_defaults(self):
        """Test for creating a new Manager object with defaults."""

        size = PictorSize(width=800, height=600)

        # Verify size.
        assert size.width == 800
        assert size.height == 600
