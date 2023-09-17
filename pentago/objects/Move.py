from enum import Enum

class Direction(Enum):
    CLOCKWISE = 1
    COUNTERCLOCKWISE = 2

class Move:
    def __init__(self, row_number : int, col_number : int, quadrant : int, direction : Direction) -> None:
        self.row_number = row_number
        self.col_number = col_number
        self.quadrant = quadrant
        self.direction = direction
