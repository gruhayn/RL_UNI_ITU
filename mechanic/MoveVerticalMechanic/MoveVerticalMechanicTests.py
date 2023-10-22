from Exceptions import AbstractMechanicExecuteMethodCalled
from mechanic.MoveVerticalMechanic.MoveVerticalMechanic import MoveVerticalMechanic
from mechanic.MoveVerticalMechanic.MoveVerticalOneStepBackMechanic import MoveVerticalOneStepBackMechanic
from mechanic.MoveVerticalMechanic.MoveVerticalOneStepMechanic import MoveVerticalOneStepMechanic
from player.Player import Player

def test_MoveVerticalMechanic_execute_raise_exception():
    mechanic = MoveVerticalMechanic()
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
    mechanic = MoveVerticalOneStepMechanic()
    player = Player("A", 11, 22)
    mechanic.configure(player.get_piece())

    mechanic.execute()

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 23

    mechanic_back = MoveVerticalOneStepBackMechanic()
    mechanic_back.configure(player.get_piece())

    mechanic_back.execute()

    assert player.get_piece().get_x() == 11
    assert player.get_piece().get_y() == 22
