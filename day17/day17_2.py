import re


def read_input(file_path: str) -> list[int]:
    with open(file_path, 'r') as fp:
        line = fp.read().strip()
    match = re.search('target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)', line)
    return [int(val) for val in match.groups()]


def count_non_direct_neg_y_vels(start_x: int, end_x: int, start_y: int, end_y: int) -> int:
    vels = set()
    for x_vel in range(end_x):
        for y_vel in range(-1, end_y, -1):
            pos = [0, 0]
            curr_x_vel = x_vel
            curr_y_vel = y_vel
            while (pos[0] <= end_x) and (pos[1] >= start_y):
                if (start_x <= pos[0] <= end_x) and (start_y <= pos[1] <= end_y):
                    vels.add((x_vel, y_vel))
                pos[0] += curr_x_vel
                pos[1] += curr_y_vel
                curr_y_vel -= 1
                curr_x_vel -= 1 if curr_x_vel else 0
    return len(vels)


def count_pos_y_vels(start_x: int, end_x: int, start_y: int, end_y: int) -> int:
    vels = set()
    for x_vel in range(end_x):
        for y_vel in range(abs(start_y)):
            pos = [0, 0]
            curr_x_vel = x_vel
            curr_y_vel = y_vel
            while (pos[0] <= end_x) and (pos[1] >= start_y):
                if (start_x <= pos[0] <= end_x) and (start_y <= pos[1] <= end_y):
                    vels.add((x_vel, y_vel))
                pos[0] += curr_x_vel
                pos[1] += curr_y_vel
                curr_y_vel -= 1
                curr_x_vel -= 1 if curr_x_vel else 0
    return len(vels)


def count_vels(start_x: int, end_x: int, start_y: int, end_y: int) -> int:
    vels = (end_x - start_x + 1) * (end_y - start_y + 1)
    vels += count_non_direct_neg_y_vels(start_x, end_x, start_y, end_y)
    vels += count_pos_y_vels(start_x, end_x, start_y, end_y)
    return vels


if __name__ == '__main__':

    start_x, end_x, start_y, end_y = read_input('input.txt')
    ans = count_vels(start_x, end_x, start_y, end_y)
    print(ans)
