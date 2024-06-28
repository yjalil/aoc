from collections import defaultdict
import numpy as np

def part1(input):
    mapper = defaultdict(lambda : [])
    seeds = input[0].split(':')[-1].strip().split(' ')
    for line in input[2:]:

        # print(f'Line => {line}')
        if 'map' in line:
            current_mapper = line.split(' ')[0]
        elif line!='' :
            mapper[current_mapper].append([line])
        # print('='*10)

    seeds_mapped = []

    for seed in seeds:
        # logs = f'{seed} => '
        seed = int(seed)
        for k,v in mapper.items():
            for map in v:
                if seed in range(int(map[0].split(' ')[1]),int(map[0].split(' ')[1]) + int(map[0].split(' ')[2])):
                    seed = int(map[0].split(' ')[0])  + seed - int(map[0].split(' ')[1])
                    # logs = logs + f'  {k} = > {seed}  '
                    break
        # print(logs)
        seeds_mapped.append(seed)
    return min(seeds_mapped)


def part2(input):
    mapper = defaultdict(lambda : [])
    input = iter(input)
    # seeds = input[0].split(':')[-1].strip().split(' ')
    def parse_seeds(seed_str):
        seeds = seed_str.split(':')[-1].strip().split(' ')
        return [np.uint32(seed) for seed in seeds]

    def generate_all_seeds(seeds):
        yield from range(seeds[0], seeds[0] + seeds[1])
        yield from range(seeds[2], seeds[2] + seeds[3])

    seeds = parse_seeds(next(input))
    next(input)
    all_seeds = generate_all_seeds(seeds)

    for line in input:
        if 'map' in line:
            current_mapper = line.split(' ')[0]
        elif line!='' :
            mapper[current_mapper].append([line])
    previous_seed = float('inf')
    for seed in all_seeds:
        seed = np.uint32(seed)
        for k,v in mapper.items():
            for map in v:
                if seed in range(np.uint32(map[0].split(' ')[1]),np.uint32(map[0].split(' ')[1]) + np.uint32(map[0].split(' ')[2])):
                    seed = np.uint32(map[0].split(' ')[0])  + seed - np.uint32(map[0].split(' ')[1])
                    break
        if seed < previous_seed:
            previous_seed = seed
            print(previous_seed)
    return previous_seed
