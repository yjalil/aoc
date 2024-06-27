import re
from collections import namedtuple, defaultdict


def part1(input):
    p = r'(\d+)'
    Round = namedtuple('Round', ['wins','haves','score'])
    rounds = []
    for line in input :
        line = line.split(':')[-1]
        winners = re.findall(p,line.split('|')[0])
        haves = re.findall(p,line.split('|')[-1])
        score  = int(2**(len(set(winners).intersection(set(haves))) - 1))
        rounds.append(Round(winners,haves,score))
        # print(Round(winners,haves,score))
    return sum(round.score for round in rounds)

def part2(input):
    p = r'(\d+)'
    Round = namedtuple('Round', ['card','wins','haves','matches'])
    rounds = []
    cards = defaultdict(int)
    for line in input:
        card = line.split(':')[0]
        line = line.split(':')[-1]
        winners = re.findall(p,line.split('|')[0])
        haves = re.findall(p,line.split('|')[-1])
        matches  = len(set(winners).intersection(set(haves)))
        rounds.append(Round(card,winners,haves,matches))
        # print(Round(card,winners,haves,matches))
    c = len(rounds)
    print(c)
    for i,r in enumerate(rounds):
        for next_card in rounds[i+1:i+int(r.matches)+1]:
            print(f'At {r.card} : {r.matches} ====> add copy of {next_card}')
            c += int(next_card.matches)
            print(c)
    return c
