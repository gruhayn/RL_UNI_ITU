import unittest

from PlayerSelector.TeamBasedSequentiallyPlayerSelector.TeamBasedSequentiallyPlayerSelector import \
    TeamBasedSequentiallyPlayerSelector
from board.Board import Board
from game.Game import Game
from player.Player import Player
from team.Team import Team


class MyTestCase(unittest.TestCase):
    def test_createGame_gameIsNotStarted_True(self):
        game = Game(None, None)

        self.assertEqual(False, game.is_started())

    def test_startGame_gameIsStarted(self):
        game = Game(None, None)

        game.start()

        self.assertEqual(True, game.is_started())

    def test_setBoard(self):
        board = Board(4, 5)
        game = Game(board)

        self.assertEqual(board, game.get_board())
        self.assertEqual(board.get_width(), game.get_board().get_width())
        self.assertEqual(board.get_height(), game.get_board().get_height())

    def test_getCurrentPlayer(self):
        players1 = [Player("11"), Player("12"), Player("13"), Player("14")]
        players2 = [Player("21"), Player("22")]
        players3 = [Player("31"), Player("32"), Player("33")]

        team1 = Team(players1)
        team2 = Team(players2)
        team3 = Team(players3)

        teams = [team1, team2, team3]

        player_selector = TeamBasedSequentiallyPlayerSelector(teams)

        game = Game(None, player_selector)

        selected_player_order = [
            "11",
            "21",
            "31",
            "12",
            "22",
            "32",
            "13",
            "21",
            "33",
            "14",
            "22",
            "31",
            "11",
            "21",
            "32"
        ]

        for i in selected_player_order:
            selectedPlayer = game.select_next_player()
            self.assertEqual(selectedPlayer.get_name(), i)



if __name__ == '__main__':
    unittest.main()
