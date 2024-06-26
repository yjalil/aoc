import re

def part1(input):
    p = r'(\d)'
    matches = [re.findall(p, x)[0] +re.findall(p, x)[-1]   for x in input]
    return sum([int(x) for x in matches])

def part2(input):
    letters = ['one',
              'two',
              'three',
              'four',
              'five',
              'six',
              'seven',
              'eight',
              'nine',
              ]
    numbers = [str(i) for i in range(1,10)]
    keys = letters + numbers
    values = numbers + numbers
    mapper = {keys[i] : values[i] for i in range(len(keys))}
    p = "|".join(map(re.escape, keys))
    matches = [int(mapper[re.findall(p, x)[0]] + mapper[re.findall(p, x)[-1]]) for x in input]
    return sum(matches)
