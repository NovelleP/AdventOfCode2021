def read_input(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as fp:
        return [[int(n) for n in line.strip()] for line in fp.readlines()]


def neighbors(row: int, col: int, visited_points: set[tuple[int, int]], energy_levels: list[list[int]]) -> list[tuple[int, int]]:
    points = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if (0 <= i < len(energy_levels)) and ((0 <= j < len(energy_levels[i]))) and ((i, j) not in visited_points) and ((i, j) != (row, col)):
                points.append((i, j))
    return points


def make_step(energy_levels: list[list[int]], flashed_points: set[tuple[int, int]]) -> int:
    pos_to_flash = {
        (i, j)
        for i, row in enumerate(energy_levels)
        for j, n in enumerate(row)
        if (n > 9) and ((i, j) not in flashed_points)
    }
    flashed_points = flashed_points | pos_to_flash
    for row, col in pos_to_flash:
        energy_levels[row][col] = 0
        for i, j in neighbors(row, col, flashed_points, energy_levels):
            energy_levels[i][j] += 1
    return len(pos_to_flash) + (make_step(energy_levels, flashed_points) if pos_to_flash else 0)


def calc_step_flashes(energy_levels: list[list[int]]) -> int:
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[i])):
            energy_levels[i][j] += 1
    return make_step(energy_levels, set())


def calc_flashes_afet_N_steps(energy_levels: list[list[int]], steps: int) -> int:
    flashes = 0
    for _ in range(steps):
        flashes += calc_step_flashes(energy_levels)
    return flashes


if __name__ == '__main__':
    energy_levels = read_input('input.txt')
    ans = calc_flashes_afet_N_steps(energy_levels, 100)
    print(ans)
