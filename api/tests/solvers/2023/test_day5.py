from api.solution import solve

def test_day5_2023_part1():
    assert solve(2023,5,1,'example1') == 35
    assert solve(2023,5,1,'input') == 379811651


def test_day5_2023_part2():
    assert solve(2023,5,2,'example2') == 46
    assert solve(2023,5,2,'input') == 27992443
