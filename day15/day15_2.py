def read_input(file_path: str) -> list[list[int]]:
    with open(file_path, 'r') as fp:
        return [[int(n) for n in line.strip()] for line in fp.readlines() if line.strip()]


def expand_matrix(matrix: list[list[int]], times: int) -> list[list[int]]:
    orig_rows, orig_cols = len(matrix), len(matrix[0])
    rows, cols = len(matrix) * times, len(matrix[0]) * times
    expanded_matrix = [[None for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            val = ((matrix[i % orig_rows][j % orig_cols]) + ((i // orig_rows) + (j // orig_cols)))
            expanded_matrix[i][j] = val if val < 10 else (val % 10) + 1
    return expanded_matrix


def manhattan(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def neighbors(row: int, col: int, matrix: list[list[int]], visited: set[tuple[int, int]]) -> list[tuple[int, int]]:
    neighs = []
    for i in range(row - 1, row + 2):
        if 0 <= i < len(matrix):
            for j in range(col - 1, col + 2):
                if (0 <= j < len(matrix[i])) and ((i, j) not in visited) and ((i, j) != (row, col)) and manhattan(row, col, i, j) == 1:
                    neighs.append((i, j))
    return neighs


def search_best_path(matrix: list[list[int]], start_row: int, start_col: int, end_row: int, end_col: int) -> int:
    distances = {(i, j): float('inf') for i in range(len(matrix)) for j in range(len(matrix[i]))}
    distances[(start_row, start_col)] = 0
    remaining = {(start_row, start_col): 0}
    visited = set()

    while remaining:
        row, col = min(remaining.items(), key=lambda t: t[1])[0]
        del remaining[(row, col)]
        visited.add((row, col))
        for i, j in neighbors(row, col, matrix, visited):
            distances[(i, j)] = min(distances[(i, j)], distances[(row, col)] + matrix[i][j])
            remaining[(i, j)] = distances[(i, j)]
    return distances[(end_row, end_col)]


if __name__ == '__main__':

    matrix = read_input('input.txt')
    expanded_matrix = expand_matrix(matrix, 5)
    ans = search_best_path(expanded_matrix, 0, 0, len(expanded_matrix) - 1, len(expanded_matrix[0]) - 1)
    print(ans)
