import re


def read_input(file_path: str) -> list[int]:
    with open(file_path, 'r') as fp:
        line = fp.read().strip()
    match = re.search('target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)', line)
    return [int(val) for val in match.groups()]


def search_max_high(start_y: int) -> int:
    init_y_vel = abs(start_y) - 1
    return (init_y_vel * (init_y_vel + 1)) // 2


if __name__ == '__main__':

    start_x, end_x, start_y, end_y = read_input('input.txt')
    ans = search_max_high(start_y)
    print(ans)
