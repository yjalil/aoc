import re
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
            mapper = {colors[i]:nums[i] for i in range(len(nums))}
            common_keys = constraint.keys() & mapper.keys()
            if any(mapper[key] > constraint[key] for key in common_keys) :
                impossible_games.append(id+1)

    return sum(set([i+1 for i in range(len(games))]).difference(set(impossible_games)))

def part2(input):
    powers = 0
    games =  [x.split(':')[1].strip() for x in input]
    for id,game in enumerate(games):
        # print(f'--------Game {id + 1}---------')
        sets= []
        for round in game.split(';'):
            colors = round.strip().split(' ')[1::2]
            colors = [x.strip(',') for x in colors]
            nums = round.strip().split(' ')[::2]
            nums = [int(x) for x in nums]
            mapper = {colors[i]:nums[i] for i in range(len(nums))}
            sets.append(mapper)
        largest_values_dict = {}

        all_keys = set().union(*(d.keys() for d in sets))

        # Iterate over each key and find the maximum value
        for key in all_keys:
            max_value = float('-inf')
            for d in sets:
                if key in d:
                    max_value = max(max_value, d[key])
            largest_values_dict[key] = max_value
        # print(math.prod(largest_values_dict.values()))
        powers = powers + math.prod(largest_values_dict.values())
    return powers
