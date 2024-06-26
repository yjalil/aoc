import argparse
import importlib

def solve(year,day,part,file):
    module = importlib.import_module(f"api.solvers.{year}.day{day}.solver")
    importlib.reload(module)
    solver = getattr(module, f'part{part}')
    with open(f'api/solvers/{year}/day{day}/{file}.txt','r') as f:
        input = f.read().split('\n')[:-1]
    return solver(input)


def main():
    parser = argparse.ArgumentParser(description='Get puzzle input')
    parser.add_argument('year', type=int, help='Year of challenge')
    parser.add_argument('day', type=str, help='Day of challenge')
    parser.add_argument('part', type=str, help='Part of challenge')
    parser.add_argument('file', type=str, help='Example or Input of challenge')


    args = parser.parse_args()
    print(solve(args.year, args.day, args.part, args.file))

if __name__ == '__main__':
    main()
