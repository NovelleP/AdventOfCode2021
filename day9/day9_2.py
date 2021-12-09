from operator import mul
from functools import reduce
from collections import defaultdict


def read_input(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as fp:
        return [[int(h) for h in line.strip()] for line in fp.readlines()]


def are_adjacent_points_higher(row_idx: int, col_idx: int, heights: list[list[int]]) -> bool:
    for i in range(row_idx - 1, row_idx + 2):
        if 0 <= i < len(heights):
            for j in range(col_idx - 1, col_idx + 2):
                if (0 <= j < len(heights[i])) and ((i, j) != (row_idx, col_idx)):
                    if heights[i][j] <= heights[row_idx][col_idx]:
                        return False
    return True


def search_low_points(heights: list[list[int]]) -> set[tuple[int, int]]:
    low_points = set()
    for row_idx in range(len(heights)):
        for col_idx in range(len(heights[row_idx])):
            if are_adjacent_points_higher(row_idx, col_idx, heights):
                low_points.add((row_idx, col_idx))
    return low_points


def manhattan_dist(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def calc_neighbors(row_idx: int, col_idx: int, heights: list[list[int]]) -> list[tuple[int, int]]:
    neighbors = []
    for i in range(row_idx - 1, row_idx + 2):
        for j in range(col_idx - 1, col_idx + 2):
            if ((i, j) != (row_idx, col_idx)) and (0 <= i < len(heights)) and (0 <= j < len(heights[i])) and (manhattan_dist(row_idx, col_idx, i, j) == 1):
                neighbors.append((i, j))
    return neighbors


def dfs(row_idx: int, col_idx: int, heights: list[list[int]], visited_points: set[tuple[int, int]], basins_memo: dict[tuple[int, int], int]):
    if (row_idx, col_idx) in visited_points:
        return 0
    elif (row_idx, col_idx) in basins_memo:
        return basins_memo[(row_idx, col_idx)]
    else:
        for i, j in calc_neighbors(row_idx, col_idx, heights):
            if (i, j) not in visited_points:
                if (heights[i][j] > heights[row_idx][col_idx]) and (heights[i][j] != 9):
                    basins_memo[(row_idx, col_idx)] += dfs(
                        i, j, heights, visited_points, basins_memo
                    )
                    visited_points.add((i, j))
        basins_memo[(row_idx, col_idx)] += 1
        return basins_memo[(row_idx, col_idx)]


def search_basin_sizes(low_points: set[tuple[int, int]], heights: list[list[int]]) -> list[int]:
    basins_memo = defaultdict(int)
    for row_idx, col_idx in low_points:
        dfs(row_idx, col_idx, heights, set(), basins_memo)
    return [basin_size for point, basin_size in basins_memo.items() if point in low_points]


if __name__ == '__main__':

    heights = read_input('input.txt')
    low_points = search_low_points(heights)
    basin_sizes = search_basin_sizes(low_points, heights)
    ans = reduce(mul, sorted(basin_sizes, reverse=True)[:3], 1)
    print(ans)
