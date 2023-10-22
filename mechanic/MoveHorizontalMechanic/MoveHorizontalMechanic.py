from Exceptions.AbstractMechanicExecuteMethodCalled import AbstractMechanicExecuteMethodCalled
from mechanic.IMechanic import IMechanic


class MoveHorizontalMechanic(IMechanic):

    def __init__(self, description: str = None):
        super().__init__(description)
        self._stepLength = None
        self._board_piece = None

    def configure(self, board_piece):
        self._board_piece = board_piece

    def execute(self):
        if  self._stepLength is None:
            raise AbstractMechanicExecuteMethodCalled("MoveHorizontalMechanic is abstract class")
        self._board_piece.set_x(self._board_piece.get_x() + self._stepLength)
