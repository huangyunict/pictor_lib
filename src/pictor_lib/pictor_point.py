"""Module that defines the PictorPoint class."""
from decimal import Decimal

from dataclasses import dataclass
from src.pictor_lib.pictor_type import DecimalUnion


@dataclass(kw_only=True)
class PictorPoint:
    """Wrap 2d point (x, y)."""

    def __init__(self, x: DecimalUnion = 0, y: DecimalUnion = 0):
        self._x = Decimal(x)
        self._y = Decimal(y)

    @property
    def x(self) -> Decimal:
        """Get the x property."""

        return self._x

    @x.setter
    def x(self, value):
        """Set the x property."""

        self._x = value

    @property
    def y(self) -> Decimal:
        """Get the y property."""

        return self._y

    @y.setter
    def y(self, value):
        """Set the y property."""

        self._y = value

    @property
    def raw_tuple(self) -> tuple[int, int]:
        """Convert to rounded int tuple which can be used in raw Pillow APIs."""

        return round(self.x), round(self.y)

    def copy(self) -> 'PictorPoint':
        """Create a new point instance by copying all fields."""

        return PictorPoint(self._x, self._y)

    def move(self, dx: DecimalUnion, dy: DecimalUnion) -> 'PictorPoint':
        """Move the point by given (dx, dy) offset."""

        self._x += dx
        self._y += dy
        return self


PictorPoint.ORIGIN = PictorPoint(0, 0)
