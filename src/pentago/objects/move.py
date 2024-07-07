
from __future__ import annotations as __
from enum import Enum as _Enum
from pentago.exceptions import OutOfBoundsException as _OutOfBoundsException
from pentago.exceptions import InvalidQuadrantException as _InvalidQuadrantException
from pentago.exceptions import GRID_MIN as _GRID_MIN
from pentago.exceptions import GRID_MAX as _GRID_MAX
from pentago.exceptions import QUAD_MIN as _QUAD_MIN
from pentago.exceptions import QUAD_MAX as _QUAD_MAX

class Direction(_Enum):
    # TODO
    """
    Dir
    """

    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1

    def __int__(self) -> int:
        return self._value_

    def __hash__(self) -> int:
        return int(self)

    def __str__(self) -> str:
        return "CLOCKWISE" if int(self) == 0 else "COUNTERCLOCKWISE"

    def __repr__(self) -> str:
        return str(self)

class Move:
    # TODO
    """
    Move
    """

    def __init__(self, row_number : int, col_number : int, quadrant : int, direction : Direction) -> None:
        if row_number > _GRID_MAX or col_number > _GRID_MAX or row_number < _GRID_MIN or col_number < _GRID_MIN:
            raise _OutOfBoundsException(row_number, col_number)
        if quadrant > _QUAD_MAX or quadrant < _QUAD_MIN:
            raise _InvalidQuadrantException(quadrant)
        self.row_number = row_number
        self.col_number = col_number
        self.quadrant = quadrant
        self.direction = direction

    def __eq__(self, o : object) -> bool:
        if not isinstance(o, Move):
            return False
        return self.row_number == o.row_number and self.col_number == o.col_number and \
            self.quadrant == o.quadrant and self.direction == o.direction

    def __neq__(self, o : object) -> bool:
        return not self == o

    def __str__(self) -> str:
        return f"Row: {self.row_number}, Column: {self.col_number}, Quadrant: {self.quadrant}," + \
            f"Direction: {self.direction}"

    def __repr__(self) -> str:
        return str(self)

    def __int__(self) -> int:
        """
        An `int` to represent this Move. The same as calling `hash()` on this object.
        """
        return hash(self)

    def __hash__(self) -> int:
        """
        Hashcode for the `Move` object. Packs values into their own unique space of bits.
        There are 6 (rows) * 6 (columns) * 4 (quadrants) * 2 (directions) = 288 possible `Move`s.
        Packing this into 9 bits, it is [row, col, quad, dir] with [3, 3, 2, 1] bits respectively.
        This hashing method is one-to-one; it will uniquely hash any given `Move`.
        """
        return (self.row_number << 6) | (self.col_number << 3) | (self.quadrant << 1) | int(self.direction)

    @staticmethod
    def unhash(move_repr : int) -> Move:
        """
        Reverse hash for the `Move` object. Unpacks bits packaged by the `hash()` function and returns
        the corresponding, unique `Move` object.
        """
        row : int = move_repr >> 6
        col : int = move_repr >> 3 & 0b111
        dir : int = move_repr & 0b1
        quad : int = move_repr >> 1 & 0b11
        return Move(row, col, quad, dir)
