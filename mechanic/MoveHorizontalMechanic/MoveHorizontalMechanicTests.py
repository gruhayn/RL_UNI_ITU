from Exceptions import AbstractMechanicExecuteMethodCalled
from mechanic.MoveHorizontalMechanic.MoveHorizontalMechanic import MoveHorizontalMechanic
from mechanic.MoveHorizontalMechanic.MoveHorizontalOneStepBackMechanic import MoveHorizontalOneStepBackMechanic
from mechanic.MoveHorizontalMechanic.MoveHorizontalOneStepMechanic import MoveHorizontalOneStepMechanic
from player.Player import Player


def test_MoveHorizontalMechanic_execute_raise_exception():
    mechanic = MoveHorizontalMechanic()
    player = Player("A", 11, 22)
    mechanic.configure(player.get_piece())

    ex = None

    try:
        mechanic.execute()
    except AbstractMechanicExecuteMethodCalled.AbstractMechanicExecuteMethodCalled as e:
        ex = e
    except Exception as e:
        raise e

    if ex is None:
        raise ex


def test_change_board_piece_x_position_with_mechanic():
    mechanic = MoveHorizontalOneStepMechanic()
    player = Player("A", 11, 22)
    mechanic.configure(player.get_piece())

    mechanic.execute()

    assert player.get_piece().get_x() == 12
    assert player.get_piece().get_y() == 22

    mechanic_back = MoveHorizontalOneStepBackMechanic()
    mechanic_back.configure(player.get_piece())

    mechanic_back.execute()

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22
