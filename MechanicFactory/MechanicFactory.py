from Enums.Enums import Mechanics
from mechanic.MoveHorizontalMechanic.MoveHorizontalOneStepBackMechanic import MoveHorizontalOneStepBackMechanic
from mechanic.MoveHorizontalMechanic.MoveHorizontalOneStepMechanic import MoveHorizontalOneStepMechanic
from mechanic.MoveVerticalMechanic.MoveVerticalOneStepBackMechanic import MoveVerticalOneStepBackMechanic
from mechanic.MoveVerticalMechanic.MoveVerticalOneStepMechanic import MoveVerticalOneStepMechanic
from player import Player


class MechanicFactory(object):

    def __init__(self):
        pass

    def get_mechanic(self, mechanic_type: Mechanics, player: Player):
        mechanic = None

        if mechanic_type == Mechanics.MoveHorizontalOneStepMechanic:
            mechanic = MoveHorizontalOneStepMechanic()
        elif mechanic_type == Mechanics.MoveHorizontalOneStepBackMechanic:
            mechanic = MoveHorizontalOneStepBackMechanic()
        elif mechanic_type == Mechanics.MoveVerticalOneStepMechanic:
            mechanic = MoveVerticalOneStepMechanic()
        elif mechanic_type == Mechanics.MoveVerticalOneStepBackMechanic:
            mechanic = MoveVerticalOneStepBackMechanic()

        if mechanic_type in (Mechanics.MoveHorizontalOneStepMechanic,
                             Mechanics.MoveHorizontalOneStepBackMechanic,
                             Mechanics.MoveVerticalOneStepMechanic,
                             Mechanics.MoveVerticalOneStepBackMechanic):

            if player.get_piece() is None:
                raise Exception("Player board piece is None")

            mechanic.configure(player.get_piece())

        return mechanic


    def get_formal_mechanic(self, mechanic_type: Mechanics):
        mechanic = None

        if mechanic_type == Mechanics.MoveHorizontalOneStepMechanic:
            mechanic = MoveHorizontalOneStepMechanic()
        elif mechanic_type == Mechanics.MoveHorizontalOneStepBackMechanic:
            mechanic = MoveHorizontalOneStepBackMechanic()
        elif mechanic_type == Mechanics.MoveVerticalOneStepMechanic:
            mechanic = MoveVerticalOneStepMechanic()
        elif mechanic_type == Mechanics.MoveVerticalOneStepBackMechanic:
            mechanic = MoveVerticalOneStepBackMechanic()


        return mechanic
