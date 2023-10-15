from PlayerSelector.IPlayerSelector import IPlayerSelector
from Utilities.SingleLinkedList.SingleLinkedList import SingleLinkedList


# Team1: player11, player12, player13
# Team2: player21, player22
# Team3: player31, player32, player33

# Selection:
#   player11,   T1 P1
#   player21,   T2 P1
#   player31,   T3 P1
#   player12,   T1 P2
#   player22,   T2 P2
#   player32,   T3 P2
#   player 13,  T1 P3
#   player21,   T2 P1
#   player33    T3 P3
#   player11,   T1 P1
#   player22,   T2 P2
#   player31,   T3 P1
#   player12,   T1 P2
#   player22,   T2 P1
#   player31,   T3 P2

class TeamBasedSequentiallyPlayerSelector(IPlayerSelector):

    def __init__(self):
        super().__init__()
        self._currentTeamIndex = None

    def set_teams(self, teams: tuple):
        super().set_teams(teams)
        self._create_single_linked_list_from_teams()
        self._currentTeamIndex = -1

    def _create_single_linked_list_from_teams(self):
        self._linked_lists = []

        for team in self._teams:
            linked_list = SingleLinkedList()
            for player in team.get_players():
                linked_list.insert(player)
            self._linked_lists.append(linked_list)

    def select_next_player(self):
        self._currentTeamIndex = self._currentTeamIndex + 1
        if self._currentTeamIndex >= len(self._linked_lists):
            self._currentTeamIndex = 0

        return self._linked_lists[self._currentTeamIndex].get_current().data

