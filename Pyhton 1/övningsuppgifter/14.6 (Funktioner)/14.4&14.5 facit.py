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


def make_list(dictionary: dict):
    list_from_dict = []
    for country in teams_dict:
        country_dict = {
            'country': country,
            'wins': teams_dict[country]['wins'],
            'draws': teams_dict[country]['draws'],
            'losses': teams_dict[country]['losses'],
            'goals_for': teams_dict[country]['goals_for'],
            'goals_against': teams_dict[country]['goals_against']
        }
        list_from_dict.append(country_dict)
    return list_from_dict


teams_list = make_list(teams_dict)


def print_table(lista: list):
    print('-'*50)
    print('| # |', 'Nation'.ljust(11), '| W | D | L | GF | GA | GD | P |')
    print('-'*50)
    counter = 1
    for country in lista:
        # Calculates goal difference and points
        country['GD'] = country['goals_for'] - country['goals_against']
        country['P'] = (country['wins'] * 3) + country['draws']
    for i in lista:
        nation = i["country"].ljust(11)
        w = str(i["wins"]).rjust(1)
        d = str(i["draws"]).ljust(1)
        l = str(i["losses"]).ljust(1)
        gf = str(i["goals_for"]).ljust(2)
        ga = str(i["goals_against"]).ljust(2)
        gd = str(i["GD"]).rjust(2)
        p = str(i["P"]).ljust(1)
        print(f'| {counter} | {nation} | {w} | {d} | {l} | {gf} | {ga} | {gd} | {p} |')
        counter += 1
    print('-' * 50)


print_table(teams_list)