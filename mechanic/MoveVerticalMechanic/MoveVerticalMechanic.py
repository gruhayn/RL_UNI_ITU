from Exceptions.AbstractMechanicExecuteMethodCalled import AbstractMechanicExecuteMethodCalled
from boardPiece import BoardPiece
from game import Game
from mechanic.IMechanic import IMechanic


class MoveVerticalMechanic(IMechanic):

    def __init__(self, description: str = None):
        super().__init__(description)
        self._stepLength = None
        self._board_piece = None

    def configure(self, board_piece):
        self._board_piece = board_piece

    def execute(self):
        if self._stepLength is None:
            raise AbstractMechanicExecuteMethodCalled("MoveVerticalMechanic is abstract class")
        self._board_piece.set_y(self._board_piece.get_y() + self._stepLength)
