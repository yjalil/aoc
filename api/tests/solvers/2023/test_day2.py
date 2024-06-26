from api.solution import solve

def test_day2_2023_part1():
    assert solve(2023,2,1,'example1') == 8
    assert solve(2023,2,1,'input') == 2061


def test_day2_2023_part2():
    assert solve(2023,2,2,'example2') == 2286
    assert solve(2023,2,2,'input') == 72596
