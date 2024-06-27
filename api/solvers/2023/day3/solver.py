import re
from collections import namedtuple

def part1(input):
    padded_input = ['.'*len(input[0])] + input + ['.'*len(input[0])]
    padded_input = ['.' + line + '.' for line in padded_input]
    p = r'(\d+)'
    pp =  "|".join(map(re.escape, ['+','-','*','#','$','%','&','@','/','=']))
    total = []
    for id,line in enumerate(padded_input[1:]):
        # print(f'==========line{id + 1 }============')
        nums = re.findall(p,line)
        start = 0
        for num in nums :

            window = padded_input[id][line.index(num, start)-1:line.index(num, start)+len(num) + 1] \
                + line[line.index(num, start)-1:line.index(num, start)+len(num)+1] \
                + padded_input[id+2][line.index(num, start)-1:line.index(num, start)+len(num)+1]
            print(f'number: {num} with window {window} => {len(re.findall(pp,window)) > 0}')
            if len(re.findall(pp,window)) > 0 :
                total.append(num)
            start = line.index(num) + len(num)
        # print(f'====>{total}')
    return sum(int(x) for x in total)

def part2(input):
    p = r'(\d+)'
    stars = []
    numbers = []
    Star = namedtuple('Star',['i','j','neighbors'])
    Number = namedtuple('Number',['value','i','j','len'])
    for i,row in enumerate(input):
        start = 0
        for num in re.findall(p,row):
            numbers.append(Number(num, i, row.index(num, start), len(num)))
            start = row.index(num, start) + len(num)
        for j,col in enumerate(row):
            if col == '*':
                stars.append(Star(i,j,[]))
    for star in stars:
        for num in numbers:
            if num.i <= star.i + 1 and star.i - 1 <= num.i :
                if star.j in range(num.j -1 ,num.j+ num.len +1):
                    star.neighbors.append(num.value)

    for s in stars:
        print(f'L:{s.i + 1} C:{s.j + 1} => {s.neighbors}')
    return sum(int(star.neighbors[0]) * int(star.neighbors[-1])
                for star in stars if len(star.neighbors) >= 2)
