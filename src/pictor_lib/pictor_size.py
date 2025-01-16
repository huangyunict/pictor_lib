"""Module that defines the PictorSize class."""
from decimal import Decimal

from dataclasses import dataclass
from src.pictor_lib.pictor_type import DecimalUnion


@dataclass(kw_only=True, frozen=True)
class PictorSize:
    """Immutable data class wrapping 2d size (width, height)."""

    width: Decimal = 0
    height: Decimal = 0

#    def __init__(self, width: DecimalUnion = 0, height: DecimalUnion = 0):
#        self.width = self._convert(width)
#        self.height = self._convert(height)

    @property
    def raw_tuple(self) -> tuple[int, int]:
        """Convert to rounded int tuple which can be used in raw Pillow APIs."""

        return round(self.width), round(self.height)

    def copy(self) -> 'PictorSize':
        """Create a new instance by copying all fields."""

        return PictorSize(width=self.width, height=self.height)

    def scale(self, ratio: DecimalUnion) -> 'PictorSize':
        """Create a new instance by scaling the width and height by given ratio."""

        return PictorSize(width=self.width * self._convert(ratio),
                          height=self.height * self._convert(ratio))

    def scale_width(self, ratio: DecimalUnion) -> 'PictorSize':
        """Create a new instance by scaling the width by given ratio."""

        return PictorSize(width=self.width * self._convert(ratio),
                          height=self.height)

    def scale_height(self, ratio: DecimalUnion) -> 'PictorSize':
        """Create a new instance by scaling the height by given ratio."""

        return PictorSize(width=self.width,
                          height=self.height * self._convert(ratio))

    def shrink_to_square(self) -> 'PictorSize':
        """Create a new square instance by shrinking the longer side to the shorter side."""

        size = min(self.width, self.height)
        return PictorSize(width=size, height=size)

    def expand_to_square(self) -> 'PictorSize':
        """Create a new square instance by expanding the shorter side to the longer side."""

        size = max(self.width, self.height)
        return PictorSize(width=size, height=size)

    def square_as_width(self) -> 'PictorSize':
        """Create a new square instance by setting the height to width."""

        return PictorSize(width=self.width, height=self.width)

    def square_as_height(self) -> 'PictorSize':
        """Create a new square instance by setting the width to height."""

        return PictorSize(width=self.height, height=self.height)

    def transpose(self) -> 'PictorSize':
        """Swap the width and height."""

        return PictorSize(width=self.height, height=self.width)

    @staticmethod
    def _convert(value: DecimalUnion) -> Decimal:
        return Decimal(value)
