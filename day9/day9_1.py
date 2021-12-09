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


def search_low_point_heights(heights: list[list[int]]) -> list[int]:
    low_points_heights = []
    for row_idx in range(len(heights)):
        for col_idx in range(len(heights[row_idx])):
            if are_adjacent_points_higher(row_idx, col_idx, heights):
                low_points_heights.append(heights[row_idx][col_idx])
    return low_points_heights


if __name__ == '__main__':

    heights = read_input('input.txt')
    low_point_heights = search_low_point_heights(heights)
    ans = sum((h + 1) for h in low_point_heights)
    print(ans)
