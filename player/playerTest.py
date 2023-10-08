import unittest

from player.Player import Player


class MyTestCase(unittest.TestCase):
    def test_createPlayerAndGetName(self):
        player: Player = Player("Natiq")
        self.assertEqual("Natiq", player.get_name())  # add assertion here


if __name__ == '__main__':
    unittest.main()
