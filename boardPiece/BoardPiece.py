class BoardPiece(object):

    def __init__(self):
        self._x = None
        self._y = None

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def has_locations(self):
        return self._x is not None and self._y is not None
