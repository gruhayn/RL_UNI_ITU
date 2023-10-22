from Enums.Enums import Mechanics
from MechanicFactory.MechanicFactory import MechanicFactory
from player.Player import Player


def test_createPlayerAndGetName():
    player: Player = Player("Natiq")
    assert ("Natiq" == player.get_name())


def test_player_not_added_mechanic_execute():
    mf = MechanicFactory()
    player = Player("A", 11, 22, mf)

    player.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22


def test_player_added_mechanics_execute():
    mf = MechanicFactory()
    player = Player("A", 11, 22, mf)

    # MoveVerticalOneStepMechanic
    player.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    player.add_mechanic(Mechanics.MoveVerticalOneStepMechanic)
    player.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    # MoveVerticalOneStepBackMechanic
    player.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    player.add_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)
    player.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    # MoveHorizontalOneStepMechanic
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    player.add_mechanic(Mechanics.MoveHorizontalOneStepMechanic)
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 13
    assert player.get_piece().get_y() == 22


    # MoveHorizontalOneStepBackMechanic
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 13
    assert player.get_piece().get_y() == 22

    player.add_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

def test_set_mechanic_factory_all_should_be_added_again():
    mf = MechanicFactory()
    player = Player("A", 11, 22, mf)

    # MoveVerticalOneStepMechanic
    player.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    player.add_mechanic(Mechanics.MoveVerticalOneStepMechanic)
    player.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    # MoveVerticalOneStepBackMechanic
    player.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    player.add_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)
    player.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    # MoveHorizontalOneStepMechanic
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    player.add_mechanic(Mechanics.MoveHorizontalOneStepMechanic)
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 13
    assert player.get_piece().get_y() == 22

    # MoveHorizontalOneStepBackMechanic
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 13
    assert player.get_piece().get_y() == 22

    player.add_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    # set mechanic factory again
    player.set_mechanic_factory(mf)

    # MoveVerticalOneStepMechanic
    player.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    player.execute_mechanic(Mechanics.MoveVerticalOneStepMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 24

    # MoveVerticalOneStepBackMechanic
    player.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    player.execute_mechanic(Mechanics.MoveVerticalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22

    # MoveHorizontalOneStepMechanic
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 13
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepMechanic)

    assert player.get_piece().get_x() == 14
    assert player.get_piece().get_y() == 22

    # MoveHorizontalOneStepBackMechanic
    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 13
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 22

    player.execute_mechanic(Mechanics.MoveHorizontalOneStepBackMechanic)

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22
