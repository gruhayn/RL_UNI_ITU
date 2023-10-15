
class BasePieceFactory(object):

    def __init__(self):
        pass

    def create_bomb_piece(self, x: int, y: int):
        raise NotImplemented

    def create_coin_piece(self, x: int, y: int):
        raise NotImplemented

