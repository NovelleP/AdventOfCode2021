import re


def read_input(file_path: str) -> tuple[list[list[str]], list[str]]:
    points = set()
    max_row = 0
    max_col = 0
    with open(file_path, 'r') as fp:
        while line := fp.readline().strip():
            point = tuple(int(e) for e in line.split(','))
            x, y = point
            max_row = max(y, max_row)
            max_col = max(x, max_col)
            points.add(point)
        foldings = [line.strip() for line in fp.readlines()]
    matrix = [['#' if (j, i) in points else '.' for j in range(max_col + 1)] for i in range(max_row + 1)]
    return matrix, foldings


def fold_to_left(matrix: list[list[str]], folding_point: int):
    for i in range(len(matrix)):
        for j in range(folding_point):
            mirror_i = i
            mirror_j = folding_point + (folding_point - j)
            matrix[i][j] = '#' if '#' in (matrix[i][j], matrix[mirror_i][mirror_j]) else '.'


def fold_to_up(matrix: list[list[str]], folding_point: int):
    for i in range(folding_point):
        for j in range(len(matrix[i])):
            mirror_i = folding_point + (folding_point - i)
            mirror_j = j
            matrix[i][j] = '#' if '#' in (matrix[i][j], matrix[mirror_i][mirror_j]) else '.'


def fold_matrix(matrix: list[list[str]], foldings: list[str]) -> list[list[str]]:
    m = re.compile('([xy])=([0-9]+)')
    rows = len(matrix)
    cols = len(matrix[0])
    for folding in foldings:
        _type, val = m.search(folding).groups()
        if _type.lower() == 'x':
            cols = min(cols, int(val))
            fold_to_left(matrix, int(val))
        elif _type.lower() == 'y':
            rows = min(rows, int(val))
            fold_to_up(matrix, int(val))
    return [[matrix[i][j] for j in range(cols)] for i in range(rows)]


if __name__ == '__main__':

    matrix, foldings = read_input('input.txt')
    ans = fold_matrix(matrix, foldings)
    for row in ans:
        print(' '.join(map(lambda v: v if v == '#' else ' ', row)))
