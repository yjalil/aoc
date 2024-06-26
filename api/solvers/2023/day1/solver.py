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
    letters_backward = [x[::-1] for x in letters]
    numbers = [str(i) for i in range(1,10)]
    keys =  letters + numbers + letters_backward
    values = numbers + numbers + numbers
    mapper = {keys[i] : values[i] for i in range(len(keys))}
    p_first = "|".join(map(re.escape, keys[:18]))
    p_last = "|".join(map(re.escape, keys[9:]))
    matches = [int(mapper[re.findall(p_first, x)[0]] + mapper[re.findall(p_last, x[::-1])[0]]) for x in input]
    return sum(matches)
