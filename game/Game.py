from PlayerSelector import IPlayerSelector
from board import Board
from player import Player


class Game(object):

    def __init__(self, board: Board, player_selector: IPlayerSelector = None):
        self._is_started = False
        self._board: Board = board
        self._player_selector = player_selector

    def select_next_player(self):
        return self._player_selector.select_next_player()

    def get_board(self):
        return self._board

    def is_started(self):
        return self._is_started

    def start(self):
        self._is_started = True
