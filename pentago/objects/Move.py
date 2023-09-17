from enum import Enum

class Direction(Enum):
    CLOCKWISE = 1
    COUNTERCLOCKWISE = 2

class Move:
    def __init__(self, x_position : int, y_position : int, quadrant : int, direction : Direction) -> None:
        self.x_position = x_position
        self.y_position = y_position
        self.quadrant = quadrant
        self.direction = direction
