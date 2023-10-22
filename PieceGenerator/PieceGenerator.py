import random

from PieceFactory import BasePieceFactory
from PieceGenerator.Location import Location
from board import Board


class PieceGenerator(object):
    def __init__(self, piece_factory: BasePieceFactory):
        self._piece_factory = piece_factory

    def get_pieces_with_locations(self, teams: tuple, bomb_count: int, coin_count: int, board: Board):
        reserved_locations = []
        players_with_no_location = []

        for team in teams:
            for player in team.get_players():
                player_piece = player.get_piece()
                if player_piece is not None and player_piece.has_locations():
                    reserved_locations.append(Location(player_piece.get_x(), player_piece.get_y()))
                else:
                    players_with_no_location.append(player)

        for player in players_with_no_location:
            piece = player.get_piece()
            defined_x = None if piece is None else piece.get_x()
            defined_y = None if piece is None else piece.get_y()

            location = self._get_random_location(reserved_locations, defined_x, defined_y, board)
            player.set_piece_x(location.get_x())
            player.set_piece_y(location.get_y())
            reserved_locations.append(location)

        bomb_pieces = []
        for i in range(bomb_count):
            location = self._get_random_location(reserved_locations, None, None, board)
            piece = self._piece_factory.create_bomb_piece(location.get_x(), location.get_y())
            bomb_pieces.append(piece)
            reserved_locations.append(location)

        coin_pieces = []
        for i in range(coin_count):
            location = self._get_random_location(reserved_locations, None, None, board)
            piece = self._piece_factory.create_coin_piece(location.get_x(), location.get_y())
            coin_pieces.append(piece)
            reserved_locations.append(location)

        return teams, bomb_pieces, coin_pieces

    def _get_random_location(self, reserved_locations: tuple, defined_x: int, defined_y: int, board: Board):
        if defined_x is not None and defined_y is not None:
            return Location(defined_x, defined_y)

        rand_x = self._calculate_rand(0, board.get_width() - 1, defined_x)
        rand_y = self._calculate_rand(0, board.get_height() - 1, defined_y)

        while any(loc.get_x() == rand_x and loc.get_y() == rand_y for loc in reserved_locations):
            rand_x = self._calculate_rand(0, board.get_width() - 1, defined_x)
            rand_y = self._calculate_rand(0, board.get_height() - 1, defined_y)

        return Location(rand_x, rand_y)

    def _calculate_rand(self, lower_bound: int, upper_bound: int, defined_val: int):
        if defined_val is not None:
            return defined_val
        else:
            return random.randint(lower_bound, upper_bound)
