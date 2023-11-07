
from __future__ import annotations as __

from pentago.objects.move import Move, Direction
from pentago.gameplay.status import GameStatus

class Board:

    def __init__(self) -> None:
        self.board_array : [[int]] = [[0] * 6] * 6

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, o : object) -> bool:
        if type(o) != type(self):
            return False

        for row in range(len(self.board_array)):
            for col in range(len(self.board_array)):
                if self.board_array[row][col] != o.board_array[row][col]:
                    return False
        return True

    def __neq__(self, o : object) -> bool:
        return not self == o

    def is_win(self, player_number : int) -> bool:
        pass

    def is_draw(self) -> bool:
        pass

    def check_win(self) -> GameStatus:
        pass

    def make_move(self, move : Move) -> Board:
        pass

    def clone(self) -> Board:
        pass

    def place_token(self, row_number : int, col_number : int, value : int) -> Board:
        pass

    def rotate_quadrant(self, quadrant : int, direction : Direction) -> Board:
        pass
