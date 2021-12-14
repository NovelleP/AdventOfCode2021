from collections import Counter


def read_input(file_path: str) -> tuple[list[str], dict[str, str]]:
    pair_to_insertion = {}
    with open(file_path, 'r') as fp:
        polymer_template = list(fp.readline().strip())
        for line in fp.readlines():
            line = line.strip()
            if line:
                pair, insertion = line.split(' -> ')
                pair_to_insertion[pair] = insertion
    return polymer_template, pair_to_insertion


def make_pair_insertions(polymer: list[str], pair_to_insertion: dict[str, str]) -> list[str]:
    new_polymer = []
    for e1, e2 in zip(polymer[:-1], polymer[1:]):
        insertion = pair_to_insertion[f'{e1}{e2}']
        new_polymer.extend([e1, insertion])
    new_polymer.append(e2)
    return new_polymer


def make_pair_insertions_N_times(polymer_template: list[str], pair_to_insertion: dict[str, str], times: int) -> int:
    for _ in range(times):
        polymer_template = make_pair_insertions(polymer_template, pair_to_insertion)
    counter = Counter(polymer_template)
    return max(counter.values()) - min(counter.values())


if __name__ == '__main__':
    polymer_template, pair_to_insertion = read_input('input.txt')
    ans = make_pair_insertions_N_times(polymer_template, pair_to_insertion, 10)
    print(ans)
