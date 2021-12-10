from collections import deque
from typing import Optional


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as fp:
        return [line.strip() for line in fp.readlines()]


def search_first_incorrect_closing_char(line: str, closing_char_to_opening_char: dict[str, str]) -> Optional[str]:
    stack = deque()
    for char in line:
        if char in closing_char_to_opening_char:
            if len(stack) == 0:
                return char
            last_opening_char = stack.pop()
            if closing_char_to_opening_char[char] != last_opening_char:
                return char
        else:
            stack.append(char)
    return None


def search_first_incorrect_closing_chars(lines: list[str], closing_char_to_opening_char: dict[str, str]) -> list[str]:
    incorrect_closing_chars = []
    for line in lines:
        char = search_first_incorrect_closing_char(line, closing_char_to_opening_char)
        if char:
            incorrect_closing_chars.append(char)
    return incorrect_closing_chars


if __name__ == '__main__':

    closing_char_to_opening_char = {')': '(', ']': '[',  '}': '{', '>': '<'}
    closing_char_to_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    lines = read_input('input.txt')
    first_incorrect_closing_characters = search_first_incorrect_closing_chars(lines, closing_char_to_opening_char)
    ans = sum(map(lambda c: closing_char_to_points[c], first_incorrect_closing_characters))
    print(ans)
