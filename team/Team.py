
class Team(object):
    def __init__(self, players: tuple):
        self._players = players

    def get_players(self):
        return self._players
