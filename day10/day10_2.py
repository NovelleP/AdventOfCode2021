from collections import deque
from typing import Optional


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as fp:
        return [line.strip() for line in fp.readlines()]


def fill_line(line: str, closing_char_to_opening_char: dict[str, str], opening_char_to_closing_char: dict[str, str]) -> list[Optional[str]]:
    stack = deque()
    for char in line:
        if char in closing_char_to_opening_char:
            if len(stack) == 0:
                return []
            last_opening_char = stack.pop()
            if closing_char_to_opening_char[char] != last_opening_char:
                return []
        else:
            stack.append(char)
    return [opening_char_to_closing_char[stack.pop()] for _ in range(len(stack))]


def fill_incomplete_lines(lines: list[str], closing_char_to_opening_char: dict[str, str]) -> list[list[str]]:
    opening_char_to_closing_char = {v: k for k, v in closing_char_to_opening_char.items()}
    filling_chars_by_line = []
    for line in lines:
        filling_chars = fill_line(line, closing_char_to_opening_char, opening_char_to_closing_char)
        if filling_chars:
            filling_chars_by_line.append(filling_chars)
    return filling_chars_by_line


def calc_sum_by_line(filling_chars_by_line: list[list[str]], closing_char_to_points: dict[str, int]) -> list[int]:
    line_sums = []
    for filling_chars in filling_chars_by_line:
        line_sum = 0
        for char in filling_chars:
            line_sum = line_sum * 5 + closing_char_to_points[char]
        line_sums.append(line_sum)
    return line_sums


if __name__ == '__main__':

    closing_char_to_opening_char = {')': '(', ']': '[',  '}': '{', '>': '<'}
    closing_char_to_points = {')': 1, ']': 2, '}': 3, '>': 4}
    lines = read_input('input.txt')
    filling_chars_by_line = fill_incomplete_lines(lines, closing_char_to_opening_char)
    line_sums = calc_sum_by_line(filling_chars_by_line, closing_char_to_points)
    line_sums.sort()
    ans = line_sums[len(line_sums) // 2]
    print(ans)
