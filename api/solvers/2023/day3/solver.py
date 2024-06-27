import re

def part1(input):
    padded_input = ['.'*len(input[0])] + input + ['.'*len(input[0])]
    padded_input = ['.' + line + '.' for line in padded_input]
    p = r'(\d+)'
    pp =  "|".join(map(re.escape, ['+','-','*','#','$','%','&','@','/','=']))
    total = []
    for id,line in enumerate(padded_input[1:]):
        print(f'==========line{id + 1 }============')
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
    # return total
    return sum([int(x) for x in total])

def part2(input):
    pass
