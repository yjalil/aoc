from api.solution import solve

def test_day4_2023_part1():
    assert solve(2023,4,1,'example1') == 13
    assert solve(2023,4,1,'input') == 24706


def test_day4_2023_part2():
    assert solve(2023,4,2,'example2') == 30
    assert solve(2023,4,2,'input') == 13114317
