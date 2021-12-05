from collections import defaultdict


def read_input(file_path: str) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    point_pairs = []
    with open(file_path, 'r') as fp:
        for line in fp.readlines():
            p1, p2 = [tuple(int(e) for e in p.split(',')) for p in line.split(' -> ')]
            point_pairs.append((p1, p2))
    return point_pairs


def expand_point(p1: tuple[int, int], p2: tuple[int, int]) -> list[tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    elif abs(x1 - x2) == abs(y1 - y2):
        x_components = range(x1, x2 + (1 if x1 < x2 else -1), 1 if x1 < x2 else -1)
        y_components = range(y1, y2 + (1 if y1 < y2 else -1), 1 if y1 < y2 else -1)
        return list(zip(x_components, y_components))


def expand_points(point_pairs: list[tuple[tuple[int, int], tuple[int, int]]]) -> defaultdict:
    point_to_covering_lines = defaultdict(lambda: 0)
    for p1, p2 in point_pairs:
        points = expand_point(p1, p2)
        for p in points:
            point_to_covering_lines[p] += 1
    return point_to_covering_lines


def search_points_covered_by_ge_than_N_lines(
        point_pairs: list[tuple[tuple[int, int], tuple[int, int]]], lines: int
) -> list[tuple[int, int]]:
    point_to_covering_lines = expand_points(point_pairs)
    return [p for p, curr_lines in point_to_covering_lines.items() if curr_lines >= lines]


if __name__ == '__main__':
    point_pairs = read_input('input.txt')
    points = search_points_covered_by_ge_than_N_lines(point_pairs, 2)
    print(len(points))
