from collections import Counter


def first_N_narutal_numbers_sum(n: int) -> int:
    return n * (n + 1) // 2


def min_fuel(positions: list[int]) -> int:
    min_pos = min(positions)
    max_pos = max(positions)
    pos_to_freq = Counter(positions)
    ans = float('inf')
    for pos in range(min_pos, max_pos + 1):
        curr_ans = sum(first_N_narutal_numbers_sum(abs(pos - curr_pos)) * freq for curr_pos, freq in pos_to_freq.items())
        ans = min(ans, curr_ans)
    return ans


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        positions = [int(pos) for pos in fp.read().strip().split(',')]

    ans = min_fuel(positions)
    print(ans)
