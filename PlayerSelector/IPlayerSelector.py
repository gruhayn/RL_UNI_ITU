class IPlayerSelector(object):

    def __init__(self, teams: tuple):
        self._teams = teams

    def select_next_player(self):
        raise NotImplemented()
