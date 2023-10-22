
from player.Player import Player
from team.Team import Team


def test_createTeam():
    players = (Player("Natiq"))
    team = Team(players)
    assert(None is not team)

def test_getPlayers():
    players = (Player("Natiq"))
    team = Team(players)
    assert (team.get_players() == players)

