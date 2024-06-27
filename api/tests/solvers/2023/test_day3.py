from api.solution import solve

def test_day3_2023_part1():
    assert solve(2023,3,1,'example1') == 4361
    assert solve(2023,3,1,'input') == 531932


def test_day3_2023_part2():
    assert solve(2023,3,2,'example2') == 467835
    assert solve(2023,3,2,'input') == 73646890
