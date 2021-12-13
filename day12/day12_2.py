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


def all_paths(graph: dict[str, set[str]], init_cave: str, final_cave: str, small_caves_to_visits: dict[str, int], small_cave_visited_two_times: bool) -> int:
    if init_cave == final_cave:
        return 1
    if init_cave.islower():
        small_caves_to_visits[init_cave] += 1
        if small_caves_to_visits[init_cave] == 2:
            small_cave_visited_two_times = True
    paths = 0
    for cave in graph[init_cave]:
        if not ((cave in small_caves_to_visits) and small_cave_visited_two_times):
            paths += all_paths(graph, cave, final_cave, small_caves_to_visits.copy(), small_cave_visited_two_times)
    return paths


if __name__ == '__main__':
    graph = read_input('input.txt')
    ans = all_paths(graph, 'start', 'end', defaultdict(int), False)
    print(ans)
