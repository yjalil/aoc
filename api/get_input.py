import requests
import os
import argparse

def download(year,day):
    cookies={'session': os.environ.get('SESSION')}
    session = requests.Session()
    session.cookies
    response = session.get(f"https://adventofcode.com/{year}/day/{day}/input",cookies=cookies)
    print(response.status_code)
    if response.status_code == 200:
        with open(f'api/solvers/{year}/day{day}/input.txt','w+') as f:
            f.write(response.text)
    else :
        print('could not download the input')

def main():
    parser = argparse.ArgumentParser(description='Get puzzle input')
    parser.add_argument('year', type=int, help='Year of challenge')
    parser.add_argument('day', type=str, help='Day of challenge')

    args = parser.parse_args()
    download(args.year, args.day)

if __name__ == '__main__':
    main()
