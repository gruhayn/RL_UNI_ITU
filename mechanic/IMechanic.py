from game import Game


class IMechanic(object):

    def __init__(self, description):
        self._description = description

    def execute(self):
        raise NotImplemented()

    def get_description(self):
        return self._description
