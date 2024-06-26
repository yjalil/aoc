import math

def part1(input):
    constraint = {
        'red': 12,
        'green': 13,
        'blue':14
    }
    impossible_games = []
    games =  [x.split(':')[1].strip() for x in input]
    for id,game in enumerate(games):
        # print(f'--------Game {id + 1}---------')
        for round in game.split(';'):
            colors = round.strip().split(' ')[1::2]
            colors = [x.strip(',') for x in colors]
            nums = round.strip().split(' ')[::2]
            nums = [int(x) for x in nums]
            mapper = dict(zip(colors,nums))
            common_keys = constraint.keys() & mapper.keys()
            if any(mapper[key] > constraint[key] for key in common_keys) :
                impossible_games.append(id+1)

    return sum(set([i+1 for i in range(len(games))]).difference(set(impossible_games)))

def part2(input):
    games = [x.split(':')[1].strip() for x in input]

    powers = 0
    for game in games:
        rounds = game.split(';')
        sets = [
            {color.strip(','): int(num) for num, color in zip(round.split()[::2], round.split()[1::2])}
            for round in rounds
        ]

        all_keys = set().union(*sets)
        largest_values_dict = {key: max(d.get(key, float('-inf')) for d in sets) for key in all_keys}

        powers += math.prod(largest_values_dict.values())

    return powers
