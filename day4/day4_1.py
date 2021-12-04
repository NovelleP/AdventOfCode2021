import re


def read_input(file_path: str) -> tuple[list, list[list[list[int]]]]:
    with open(file_path, 'r') as fp:
        numbers = [int(n) for n in fp.readline().strip().split(',')]
        boards = [
            [
                [int(n) for n in row.split()]
                for row in board.split('\n')
            ]
            for board in re.split('\n{2}', fp.read().strip())
        ]

    return numbers, boards


def search_number_in_board(target: int, board_info: dict) -> bool:
    board = board_info['board']
    for row_idx, row in enumerate(board):
        for col_idx, number in enumerate(row):
            if number == target:
                board_info['rows'][row_idx] += 1
                if board_info['rows'][row_idx] == len(row):
                    return True
                board_info['cols'][col_idx] += 1
                if board_info['cols'][col_idx] == len(board):
                    return True
    return False


def calc_score(board: list[list[int]], last_number: int, visited_numbers: set[int]) -> int:
    non_visited_sum = sum(n for row in board for n in row if n not in visited_numbers)
    return last_number * non_visited_sum


def search_best_board(numbers: list[int], boards: list[list[list[int]]]) -> int | None:
    boards_info = [
        {
            'board': board,
            'rows': [0 for _ in board],
            'cols': [0 for _ in board[0]]
        }
        for board in boards
    ]
    visited_numbers = set()
    for number in numbers:
        visited_numbers.add(number)
        for board_info in boards_info:
            result = search_number_in_board(number, board_info)
            if result:
                return calc_score(board_info['board'], number, visited_numbers)
    return None


if __name__ == '__main__':

    numbers, boards = read_input('input.txt')
    ans = search_best_board(numbers, boards)
    print(ans)
