"""Module that defines the PictorRect class."""
from decimal import Decimal

from src.pictor_lib.pictor_point import PictorPoint
from src.pictor_lib.pictor_size import PictorSize


class PictorRect:
    """Wrap a rectangle as the top-left point and the non-negative size."""

    def __init__(self, point: PictorPoint, size: PictorSize):
        self._point = point
        self._size = size

    @property
    def top(self) -> Decimal:
        return self._point.y

    @property
    def bottom(self) -> Decimal:
        return self._point.y + self._size.height

    @property
    def left(self) -> Decimal:
        return self._point.x

    @property
    def right(self) -> Decimal:
        return self._point.x + self._size.width

    @property
    def top_left(self) -> PictorPoint:
        return self._point

    @property
    def top_center(self) -> PictorPoint:
        return self._point.move_x(self._size.width / 2)

    @property
    def top_right(self) -> PictorPoint:
        return self._point.move_x(self._size.width)

    @property
    def left_center(self) -> PictorPoint:
        return self._point.move_y(self._size.height / 2)

    @property
    def center(self) -> PictorPoint:
        return self._point.move_x(self._size.width / 2).move_y(
            self._size.height / 2)

    @property
    def right_center(self) -> PictorPoint:
        return self._point.move_x(self._size.width).move_y(self._size.height /
                                                           2)

    @property
    def bottom_left(self) -> PictorPoint:
        return self._point.move_y(self._size.height)

    @property
    def bottom_center(self) -> PictorPoint:
        return self._point.move_x(self._size.width / 2).move_y(
            self._size.height)

    @property
    def bottom_right(self) -> PictorPoint:
        return self._point.move_x(self._size.width).move_y(self._size.height)

    @property
    def size(self) -> PictorSize:
        return self._size

    def __repr__(self) -> str:
        return '{:0.2f}x{:0.2f}+{:0.2f}+{:0.2f}'.format(self.size.width,
                                                        self.size.height,
                                                        self.top_left.x,
                                                        self.top_right.y)
