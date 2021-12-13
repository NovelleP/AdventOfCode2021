from collections import defaultdict


def read_input(file_path: str) -> dict[str, set[str]]:
    graph = defaultdict(set)
    with open(file_path, 'r') as fp:
        for line in fp.readlines():
            cave1, cave2 = line.strip().split('-')
            if (cave1 != 'end') and (cave2 != 'start'):
                graph[cave1].add(cave2)
            if (cave2 != 'end') and (cave1 != 'start'):
                graph[cave2].add(cave1)
    return graph


def all_paths(graph: dict[str, set[str]], init_cave: str, final_cave: str, visited: set[str]) -> int:
    if init_cave == final_cave:
        return 1
    return sum(
        all_paths(graph, cave, final_cave, (visited | {cave}) if cave.islower() else visited)
        for cave in graph[init_cave]
        if cave not in visited
    )


if __name__ == '__main__':
    graph = read_input('input.txt')
    ans = all_paths(graph, 'start', 'end', set())
    print(ans)
