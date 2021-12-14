from collections import Counter, defaultdict


def read_input(file_path: str) -> tuple[list[str], dict[tuple[str, str], str]]:
    pair_to_insertion = {}
    with open(file_path, 'r') as fp:
        polymer_template = list(fp.readline().strip())
        for line in fp.readlines():
            line = line.strip()
            if line:
                pair, insertion = line.split(' -> ')
                pair_to_insertion[tuple(pair)] = insertion
    return polymer_template, pair_to_insertion


def make_pair_insertions(
        pair_to_freq: dict[tuple[str, str], int], pair_to_insertion: dict[tuple[str, str], str]
) -> dict[tuple[str, str], int]:
    new_pair_to_freq = defaultdict(int)
    for pair, freq in pair_to_freq.items():
        insertion = pair_to_insertion[pair]
        e1, e2 = pair
        new_pair_to_freq[(e1, insertion)] += freq
        new_pair_to_freq[(insertion, e2)] += freq
    return new_pair_to_freq


def calc_element_freq(pair_to_freq: dict[tuple[str, str], int]) -> dict[str, int]:
    element_to_freq = defaultdict(int)
    for (e1, e2), freq in pair_to_freq.items():
        element_to_freq[e1] += freq
        element_to_freq[e2] += freq
    for e, freq in element_to_freq.items():
        if (freq % 2) != 0:
            freq += 1
        element_to_freq[e] = freq // 2
    return element_to_freq


def make_pair_insertions_N_times(
        polymer_template: list[str], pair_to_insertion: dict[tuple[str, str], str], times: int
) -> int:
    pair_to_freq = Counter([tuple(pair) for pair in zip(polymer_template[:-1], polymer_template[1:])])
    for _ in range(times):
        pair_to_freq = make_pair_insertions(pair_to_freq, pair_to_insertion)
    element_to_freq = calc_element_freq(pair_to_freq)
    return max(element_to_freq.values()) - min(element_to_freq.values())


if __name__ == '__main__':
    polymer_template, pair_to_insertion = read_input('input.txt')
    ans = make_pair_insertions_N_times(polymer_template, pair_to_insertion, 40)
    print(ans)
