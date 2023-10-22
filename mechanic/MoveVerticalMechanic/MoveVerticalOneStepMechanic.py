from mechanic.MoveVerticalMechanic.MoveVerticalMechanic import MoveVerticalMechanic


class MoveVerticalOneStepMechanic(MoveVerticalMechanic):

    def __init__(self, description: str = None):
        description = "Bir addim yuxari"
        super().__init__(description)

    def configure(self, board_piece):
        super().configure(board_piece)
        self._stepLength = 1
