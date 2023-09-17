
class OutOfBoundsException(Exception):
    def __init__(self, x_pos : int, y_pos : int):
        super(f"The position (${x_pos}, ${y_pos}) is out of bounds for the board.")

class InvalidPlacementException(Exception):
    def __init__(self, x_pos : int, y_pos : int, player_number : int):
        super(f"Position (${x_pos}, ${y_pos}) is already occupied by player ${player_number}.")

class InvalidQuadrantException(Exception):
    def __init__(self, quadrant : int):
        super(f"Expected quadrant to be between 1 and 4, recieved ${quadrant}.")

class InvalidArgumentException(Exception):
    def __init__(self, expected_type : type, actual_type : type):
        super(f"Expected argument of type ${expected_type}, received ${actual_type}.")
