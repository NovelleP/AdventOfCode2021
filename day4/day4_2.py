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
    last_winning_board = None
    last_number = None
    last_visited_numbers = None
    visited_numbers = set()
    winning_board_idxs = set()
    for number in numbers:
        if len(winning_board_idxs) == len(boards):
            break
        visited_numbers.add(number)
        for idx, board_info in enumerate(boards_info):
            result = search_number_in_board(number, board_info)
            if result and idx not in winning_board_idxs:
                winning_board_idxs.add(idx)
                last_winning_board = board_info['board']
                last_number = number
                last_visited_numbers = visited_numbers.copy()

    return calc_score(last_winning_board, last_number, last_visited_numbers) if last_winning_board else None


if __name__ == '__main__':

    numbers, boards = read_input('input.txt')
    ans = search_best_board(numbers, boards)
    print(ans)
