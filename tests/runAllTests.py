
from inspect import getmembers, isfunction

import pytest

import board.boardTest as boardTest
import boardPiece.BoardPieceTests as BoardPieceTests
import game.gameTest as gameTest
import player.playerTest as playerTest
import PlayerSelector.TeamBasedSequentiallyPlayerSelector.TeamBasedSequentiallyPlayerSelectorTests \
    as TeamBasedSequentiallyPlayerSelectorTests
import team.teamTest as teamTest
from BoardPieceHandler import BoardPieceHandlerTests
from GameCreator import GameCreatorTests
from MechanicFactory import MechanicFactoryTests
from PieceFactory.BasicPieceFactory import BasicPieceFactoryTests
from PieceGenerator import PieceGeneratorTests
from boardPiece.BombBoardPiece import BombBoardPieceTests
from boardPiece.CoinBoardPiece import CoinBoardPieceTests
from boardPiece.PlayerBoardPiece import PlayerBoardPieceTests
from mechanic.MoveHorizontalMechanic import MoveHorizontalMechanicTests
from mechanic.MoveVerticalMechanic import MoveVerticalMechanicTests

# assertions will raise an error.
# there is no error then nothing will happen

tests = [
    boardTest,
    BoardPieceTests,
    gameTest,
    playerTest,
    TeamBasedSequentiallyPlayerSelectorTests,
    teamTest,
    PlayerBoardPieceTests,
    CoinBoardPieceTests,
    BombBoardPieceTests,
    BasicPieceFactoryTests,
    PieceGeneratorTests,
    GameCreatorTests,
    BoardPieceHandlerTests,
    MoveHorizontalMechanicTests,
    MoveVerticalMechanicTests,
    MechanicFactoryTests
]

for testScenarios in tests:
    for member in getmembers(testScenarios, isfunction):
        method = member[1]
        method()


