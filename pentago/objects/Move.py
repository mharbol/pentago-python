from __future__ import annotations
from enum import Enum

class Direction(Enum):
    CLOCKWISE = 0
    COUNTERCLOCKWISE = 1

    def __int__(self) -> int:
        return self._value_

    def __hash__(self) -> int:
        return int(self)

class Move:
    def __init__(self, row_number : int, col_number : int, quadrant : int, direction : Direction) -> None:
        # TODO out of bounds checks
        self.row_number = row_number
        self.col_number = col_number
        self.quadrant = quadrant
        self.direction = direction

    def __hash__(self) -> int:
        """
        Hashcode for the `Move` object. Packs values into their own unique space of bits.
        There are 6 (rows) * 6 (columns) * 4 (quadrants) * 2 (directions) = 288 possible `Move`s.
        Packing this into 9 bits, it is [row, col, quad, dir] with [3, 3, 2, 1] bits respectively.
        """
        return (self.row_number << 6) | (self.col_number << 3) | (self.quadrant << 1) | int(self.direction)

    def __eq__(self, o : object) -> bool:
        if type(o) != type(self):
            return False
        return self.row_number == o.row_number and self.col_number == o.col_number and \
            self.quadrant == o.quadrant and self.direction == o.direction

    def __neq__(self, o : object) -> bool:
        return not self == o

    def __str__(self) -> str:
        return f"Row: ${self.row_number}, Column: ${self.col_number}, Quadrant: ${self.quadrant}," + \
            f"Direction: ${self.direction}"

    def __repr__(self) -> str:
        return str(self)

    def __int__(self) -> int:
        return hash(self)

    @staticmethod
    def unhash(move_repr : int) -> Move:
        row : int = move_repr >> 6
        col : int = move_repr >> 3 & 0b111
        dir : int = move_repr & 0b1
        quad : int = move_repr >> 1 & 0b11
        return Move(row, col, quad, dir)
