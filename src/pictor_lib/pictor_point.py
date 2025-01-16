"""Module that defines the PictorPoint class."""
from decimal import Decimal

from dataclasses import dataclass
from src.pictor_lib.pictor_type import DecimalUnion


@dataclass(frozen=True)
class PictorPoint:
    """Immutable data class wrapping 2d point (x, y)."""

    x: Decimal = 0
    y: Decimal = 0

    @property
    def raw_tuple(self) -> tuple[int, int]:
        """Convert to rounded int tuple which can be used in raw Pillow APIs."""

        return round(self.x), round(self.y)

    def copy(self) -> 'PictorPoint':
        """Create a new instance by copying all fields."""

        return PictorPoint(x=self.x, y=self.y)

    def set_x(self, x: DecimalUnion) -> 'PictorPoint':
        """Return a new instance with updated x property."""

        return PictorPoint(x=x, y=self.y)

    def set_y(self, y: DecimalUnion) -> 'PictorPoint':
        """Return a new instance with updated y property."""

        return PictorPoint(x=self.x, y=y)

    def move(self, dx: DecimalUnion, dy: DecimalUnion) -> 'PictorPoint':
        """Return a new instance by moving by given (dx, dy) offset."""

        return PictorPoint(x=self.x + dx, y=self.y + dy)

    @staticmethod
    def _convert(value: DecimalUnion) -> Decimal:
        return Decimal(value)


PictorPoint.ORIGIN = PictorPoint(x=0, y=0)
