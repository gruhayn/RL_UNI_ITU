from boardPiece.BoardPiece import BoardPiece


class PlayerBoardPiece(BoardPiece):

    def __init__(self, name):
        super().__init__()
        self._name = name

    def get_name(self):
        return self._name