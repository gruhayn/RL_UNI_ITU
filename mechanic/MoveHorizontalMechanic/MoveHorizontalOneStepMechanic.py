from mechanic.MoveHorizontalMechanic.MoveHorizontalMechanic import MoveHorizontalMechanic


class MoveHorizontalOneStepMechanic(MoveHorizontalMechanic):

    def __init__(self, description: str = None):
        description = "Bir addim saga"
        super().__init__(description)

    def configure(self, board_piece):
        super().configure(board_piece)
        self._stepLength = 1
