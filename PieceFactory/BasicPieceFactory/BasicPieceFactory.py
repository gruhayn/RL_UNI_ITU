from PieceFactory.BasePieceFactory import BasePieceFactory
from boardPiece.BombBoardPiece.BombBoardPiece import BombBoardPiece
from boardPiece.CoinBoardPiece.CoinBoardPiece import CoinBoardPiece


class BasicPieceFactory(BasePieceFactory):

    def __init__(self):
        super().__init__()

    def create_bomb_piece(self, x: int, y: int):
        piece = BombBoardPiece()
        piece.set_x(x)
        piece.set_y(y)
        return piece

    def create_coin_piece(self, x: int, y: int):
        piece = CoinBoardPiece()
        piece.set_x(x)
        piece.set_y(y)
        return piece