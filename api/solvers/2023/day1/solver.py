import re

def part1(input):
    p = r'(\d)'
    matches = [re.findall(p, x)[0] +re.findall(p, x)[-1]   for x in input]
    return sum([int(x) for x in matches])

def part2(input):
    #overlapping nonsense not covered in example so should check backwards for last number
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
    keys =  letters + numbers + [x[::-1] for x in letters]
    values = numbers * 3
    mapper = dict(zip(keys,values))
    p_first = "|".join(map(re.escape, keys[:18]))
    p_last = "|".join(map(re.escape, keys[9:]))
    matches = [int(mapper[re.findall(p_first, x)[0]] + mapper[re.findall(p_last, x[::-1])[0]]) for x in input]
    return sum(matches)
