
GRID_MIN : int = 0
GRID_MAX : int = 5
QUAD_MIN : int = 1
QUAD_MAX : int = 4

class OutOfBoundsException(Exception):
    def __init__(self, row_number : int, col_number : int):
        super(f"The position ({row_number}, {col_number}) is out of bounds for the board.")

class InvalidPlacementException(Exception):
    def __init__(self, rown_number : int, col_number : int, player_number : int):
        super(f"Position ({rown_number}, {col_number}) is already occupied by player {player_number}.")

class InvalidQuadrantException(Exception):
    def __init__(self, quadrant : int):
        super(f"Expected quadrant to be between {QUAD_MIN} and {QUAD_MAX}, recieved {quadrant}.")

class InvalidArgumentException(Exception):
    def __init__(self, expected_type : type, actual_type : type):
        super(f"Expected argument of type {expected_type}, received {actual_type}.")
