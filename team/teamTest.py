import unittest

from player.Player import Player
from team.Team import Team


class MyTestCase(unittest.TestCase):
    def test_createTeam(self):
        players = (Player("Natiq"))
        team = Team(players)
        self.assertNotEqual(None, team)

    def test_getPlayers(self):
        players = (Player("Natiq"))
        team = Team(players)
        self.assertEqual(team.get_players(), players)


if __name__ == '__main__':
    unittest.main()
