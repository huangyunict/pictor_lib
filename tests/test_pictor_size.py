"""Test module for the class PictorSize."""

from assertpy import assert_that

from src.pictor_lib.pictor_size import PictorSize


class TestPictorSize:
    """Tests for the class PictorSize."""

    def test_new_with_defaults(self):
        """Test for creating a new object with defaults."""

        size = PictorSize()

        # Verify size.
        assert_that(size.width).is_equal_to(0)
        assert_that(size.height).is_equal_to(0)

    def test_new_with_values(self):
        """Test for creating a new object with values."""

        size = PictorSize(width=800, height=600)

        # Verify size.
        assert_that(size.width).is_equal_to(800)
        assert_that(size.height).is_equal_to(600)

    def test_setters(self):
        """Test for creating a new object with values."""

        old_size = PictorSize(width=67, height=42)
        new_size = old_size.set_width(800).set_height(600)

        # Verify size.
        assert_that(new_size).is_not_same_as(old_size)
        assert_that(new_size.width).is_equal_to(800)
        assert_that(new_size.height).is_equal_to(600)

    def test_scale(self):
        pass

    def test_scale_width(self):
        pass

    def test_scale_height(self):
        pass

    def test_shrink_to_square(self):
        pass

    def test_expand_to_square(self):
        pass
