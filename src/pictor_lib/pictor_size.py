from decimal import Decimal


class PictorSize(tuple[Decimal, Decimal]):
    """Wrap 2d size (width x height)."""

    def __new__(cls,
                width: int | float | Decimal = 0,
                height: int | float | Decimal = 0):
        return tuple.__new__(PictorSize, (Decimal(width), Decimal(height)))

    @property
    def width(self) -> Decimal:
        return self[0]

    @property
    def height(self) -> Decimal:
        return self[1]
