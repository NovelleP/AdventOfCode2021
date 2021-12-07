from collections import Counter


def min_fuel(positions: list[int]) -> int:
    pos_to_freq = Counter(positions)
    ans = float('inf')
    for pos in pos_to_freq:
        curr_ans = sum(abs(pos - curr_pos) * freq for curr_pos, freq in pos_to_freq.items())
        ans = min(ans, curr_ans)
    return ans


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        positions = [int(pos) for pos in fp.read().strip().split(',')]

    ans = min_fuel(positions)
    print(ans)
