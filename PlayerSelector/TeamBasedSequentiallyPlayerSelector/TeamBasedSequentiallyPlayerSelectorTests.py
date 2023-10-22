
from PlayerSelector.TeamBasedSequentiallyPlayerSelector.TeamBasedSequentiallyPlayerSelector import \
    TeamBasedSequentiallyPlayerSelector
from player.Player import Player
from team.Team import Team


def test_createTeamBasedSequentiallyPlayerSelector():
    teams = []
    player_selector = TeamBasedSequentiallyPlayerSelector()
    player_selector.set_teams(teams)
    assert (player_selector is not None)
    assert isinstance(player_selector, TeamBasedSequentiallyPlayerSelector)

def test_getNextPlayer():
    players1 = [Player("11"), Player("12"), Player("13")]
    players2 = [Player("21"), Player("22"), Player("23")]

    team1 = Team(players1)
    team2 = Team(players2)

    teams = [team1, team2]

    player_selector = TeamBasedSequentiallyPlayerSelector()
    player_selector.set_teams(teams)
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("11").get_name())


def test_getNextPlayerMultiple():
    players1 = [Player("11"), Player("12"), Player("13")]
    players2 = [Player("21"), Player("22")]
    players3 = [Player("31"), Player("32"), Player("33")]



    team1 = Team(players1)
    team2 = Team(players2)
    team3 = Team(players3)

    teams = [team1, team2, team3]

    player_selector = TeamBasedSequentiallyPlayerSelector()
    player_selector.set_teams(teams)
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("11").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("21").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("31").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert(selectedPlayer.get_name() == Player("12").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("22").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("32").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("13").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("21").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("33").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("11").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("22").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("31").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("12").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("21").get_name())
    selectedPlayer = player_selector.select_next_player()
    assert (selectedPlayer.get_name() == Player("32").get_name())

def test_getNextPlayerMultiple2():
    players1 = [Player("11"), Player("12"), Player("13"), Player("14")]
    players2 = [Player("21"), Player("22")]
    players3 = [Player("31"), Player("32"), Player("33")]



    team1 = Team(players1)
    team2 = Team(players2)
    team3 = Team(players3)

    teams = [team1, team2, team3]

    player_selector = TeamBasedSequentiallyPlayerSelector()
    player_selector.set_teams(teams)

    selected_player_order = [
        "11",
        "21",
        "31",
        "12",
        "22",
        "32",
        "13",
        "21",
        "33",
        "14",
        "22",
        "31",
        "11",
        "21",
        "32"
    ]

    for i in selected_player_order:
        selectedPlayer = player_selector.select_next_player()
        assert (selectedPlayer.get_name() == i)


