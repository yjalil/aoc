from api.solution import solve

def test_day1_2023_part1():
    assert solve(2023,1,1,'example1') == 142
    assert solve(2023,1,1,'input') == 56042


def test_day1_2023_part2():
    assert solve(2023,1,2,'example2') == 281
    assert solve(2023,1,1,'input') == 55358
