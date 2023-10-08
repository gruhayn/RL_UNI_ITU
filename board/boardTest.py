import unittest

from board.Board import Board


class MyTestCase(unittest.TestCase):
    def test_createBoard(self):
        width: int = 4
        height: int = 5
        board = Board(width, height)

        self.assertEqual(width, board.get_width())
        self.assertEqual(height, board.get_height())
        self.assertNotEqual(width, board.get_height())
        self.assertNotEqual(height, board.get_width())


if __name__ == '__main__':
    unittest.main()
