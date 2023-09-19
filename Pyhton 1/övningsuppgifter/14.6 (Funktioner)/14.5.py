teams_dict = {
    'Brazil':
        {'wins': 2, 'draws': 1, 'losses': 0, 'goals_for': 5, 'goals_against': 1},
    'Serbia':
        {'wins': 1, 'draws': 0, 'losses': 2, 'goals_for': 2, 'goals_against': 4},
    'Switzerland':
        {'wins': 1, 'draws': 2, 'losses': 0, 'goals_for': 5, 'goals_against': 4},
    'Costa Rica':
        {'wins': 0, 'draws': 1, 'losses': 2, 'goals_for': 2, 'goals_against': 5}
}

teams_list = [{'country': key, 'wins': value['wins'], 'draws': value['draws'], 'losses': value['losses'],
               'goals_for': value['goals_for'], 'goals_against': value['goals_against']}
              for key, value in teams_dict.items()]


# Funktion som tar en nestlad dict och antar att nycklarna är länder och value är statistik. funktionen gör sedan
# dicten till en lista
def make_kist(dict: dict):
    result_list = [
        {'country': key, **value}
        for key, value in dict.items()
    ]
    return result_list


new_list = make_kist(teams_dict)


def print_table(list: list):
    for country in list:
        # Calculates goal difference and points
        country['GD'] = country['goals_for'] - country['goals_against']
        country['P'] = (country['wins'] * 3) + country['draws']

    print('−' * 50)
    print('| # |', 'Nation'.center(10), '|', ' W | D | L | GF | GA | GD | P |')
    print('−' * 50)
    print('| 1 |', str(list[0]['country']).center(10), '|', f'{list[0]["wins"]} | {list[0]["draws"]} | {list[0]["losses"]} | {list[0]["goals_for"]} | {list[0]["goals_against"]} | {list[0]["GD"]} | {list[0]["P"]}')


print(print_table(teams_list))

"""−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−          """
"""| # | Nation      | W | D | L | GF | GA | GD | P |               """
"""−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−          """
"""| 1 | Brazil | 2 | 1 | 0 | 5 | 1 | 4 | 7 |             """
"""| 2 | Serbia | 1 | 0 | 2 | 2 | 4 | −2 | 3 |            """
"""| 3 | Switzerland | 1 | 2 | 0 | 5 | 4 | 1 | 5 |   """
"""| 4 | Costa Rica  | 0 | 1 | 2 | 2 | 5 | −3 | 1 |             """
"""−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−          """