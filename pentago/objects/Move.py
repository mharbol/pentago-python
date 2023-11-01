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

    def __int__(self) -> int:
        return hash(self)
