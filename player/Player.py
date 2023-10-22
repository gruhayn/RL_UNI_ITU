from Enums.Enums import Mechanics
from MechanicFactory import MechanicFactory
from boardPiece.PlayerBoardPiece.PlayerBoardPiece import PlayerBoardPiece


class Player(object):
    def __init__(self,
                 name: str,
                 x: int = None,
                 y: int = None,
                 mechanic_factory: MechanicFactory = None,
                 mechanic_types: set = None):

        self._name = name

        self._board_piece = PlayerBoardPiece(name)
        self.set_piece_x(x)
        self.set_piece_y(y)

        self._mechanic_factory = None
        self._mechanic_types = None

        self._reset_mechanics()
        self._set_mechanic_types(mechanic_types)
        self.set_mechanic_factory(mechanic_factory)

    def _set_mechanic_types(self, mechanic_types):
        if mechanic_types is None:
            self._mechanic_types = set()
        else:
            self._mechanic_types = mechanic_types

    def set_mechanic_factory(self, mechanic_factory):
        self._mechanic_factory = mechanic_factory
        self._reset_mechanics()

        if self._mechanic_factory is not None:
            for mechanic_type in self._mechanic_types:
                self.add_mechanic(mechanic_type)

    def _reset_mechanics(self):
        self._mechanics = {}

    def add_mechanic(self, mechanic_type: Mechanics):
        self._mechanic_types.add(mechanic_type)
        self._mechanics[mechanic_type] = self._mechanic_factory.get_mechanic(mechanic_type, self)

    def execute_mechanic(self, mechanic_type: Mechanics):
        mechanic = self._mechanics.get(mechanic_type)

        if mechanic is None:
            return

        mechanic.execute()

    def get_name(self) -> str:
        return self._name

    def get_piece(self):
        return self._board_piece

    def set_piece_x(self, x):
        self._board_piece.set_x(x)

    def set_piece_y(self, y):
        self._board_piece.set_y(y)
