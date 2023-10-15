class IPlayerSelector(object):

    def __init__(self):
        self._teams = None

    def set_teams(self, teams: tuple):
        self._teams = teams

    def select_next_player(self):
        raise NotImplemented()
