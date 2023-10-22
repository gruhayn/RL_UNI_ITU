from Enums.Enums import Mechanics
from MechanicFactory.MechanicFactory import MechanicFactory
from player.Player import Player


def test_mechanic_factory_MoveMechanics():
    mf = MechanicFactory()
    player = Player("A", 11, 22)

    vert_mechanic = mf.get_mechanic(Mechanics.MoveVerticalOneStepMechanic, player)

    vert_mechanic.execute()
    vert_mechanic.execute()

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 24

    vert_mechanic_back = mf.get_mechanic(Mechanics.MoveVerticalOneStepBackMechanic, player)

    vert_mechanic_back.execute()

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    horz_mechanic = mf.get_mechanic(Mechanics.MoveHorizontalOneStepMechanic, player)

    horz_mechanic.execute()
    horz_mechanic.execute()

    assert player.get_piece().get_x() == 13
    assert player.get_piece().get_y() == 23

    horz_mechanic_back = mf.get_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic, player)

    horz_mechanic_back.execute()

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 23