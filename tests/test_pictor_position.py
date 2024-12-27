"""Test module for the class PictorPosition."""
import configparser
import json
from pathlib import Path

from src.pictor_lib.pictor_position import PictorPosition


class TestPictorPosition:
    """Tests for the class PictorPosition."""

    def test_new_position_with_defaults(self):
        """Test for creating a new object with defaults."""

        position = PictorPosition()

        # Verify position.
        assert position.x == 0
        assert position.y == 0

    def test_new_position_with_value(self):
        """Test for creating a new object with defaults."""

        position = PictorPosition(x=67, y=42)

        # Verify position.
        assert position.x == 67
        assert position.y == 42
