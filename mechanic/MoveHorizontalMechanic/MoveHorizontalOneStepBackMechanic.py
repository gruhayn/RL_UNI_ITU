from mechanic.MoveHorizontalMechanic.MoveHorizontalMechanic import MoveHorizontalMechanic


class MoveHorizontalOneStepBackMechanic(MoveHorizontalMechanic):

    def __init__(self, description: str = None):
        description = "Bir addim sola"
        super().__init__(description)

    def configure(self, board_piece):
        super().configure(board_piece)
        self._stepLength = -1
