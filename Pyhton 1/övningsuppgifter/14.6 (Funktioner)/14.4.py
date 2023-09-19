teams = {
    'Brazil': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Serbia': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Switzerland': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Costa Rica': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    }
}


def add_game(home_team: str, home_score: int, away_team: str, away_score: int):
    if home_team not in teams or away_team not in teams:
        print('One of the teams is not in the dictionary')
        return
    if home_score > away_score:
        teams[home_team]['wins'] += 1
        teams[away_team]['losses'] += 1
    elif home_score < away_score:
        teams[away_team]['wins'] += 1
        teams[home_team]['losses'] += 1
    else:
        teams[home_team]['draws'] += 1
        teams[away_team]['draws'] += 1

    teams[home_team]['goals_for'] += home_score
    teams[home_team]['goals_against'] += away_score

    teams[away_team]['goals_for'] += away_score
    teams[away_team]['goals_against'] += home_score


add_game('Costa Rica', 0, 'Serbia', 1)
add_game('Brazil', 1, 'Switzerland', 1)
add_game('Brazil', 2, 'Costa Rica', 0)
add_game('Serbia', 1, 'Switzerland', 2)
add_game('Serbia', 0, 'Brazil', 2)
add_game('Switzerland', 2, 'Costa Rica', 2)

for team, stats in teams.items():
    print(f"{team}: {stats}")
print(teams)