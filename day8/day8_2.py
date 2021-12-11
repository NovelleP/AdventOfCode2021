from collections import defaultdict, Counter


def read_input(file_path: str) -> list[tuple[list[str], list[str]]]:
    patterns_displayed_pairs = []
    with open(file_path, 'r') as fp:
        for line in fp.readlines():
            patterns, displayed = line.split('|')
            patterns = patterns.strip().split()
            displayed = displayed.strip().split()
            patterns_displayed_pairs.append((patterns, displayed))
    return patterns_displayed_pairs


def invert_dict(d: dict) -> dict:
    invert_dict = defaultdict(set)
    for k, v in d.items():
        invert_dict[v].add(k)
    return invert_dict


def solve_display(
        patterns: list[str], freq_to_segments: dict[int, set[str]], neighbors_to_segments: dict[int, set[str]]
) -> dict[str, str]:
    bad_segment_to_freq = Counter(list(''.join(patterns)))
    freq_to_bad_segments = invert_dict(bad_segment_to_freq)

    bad_segment_to_segment = {}
    # non ambiguous segments
    for freq, segments in freq_to_segments.items():
        if len(segments) == 1:
            segment = next(iter(segments))
            bad_segment = freq_to_bad_segments[freq].pop()
            bad_segment_to_segment[bad_segment] = segment
            del freq_to_bad_segments[freq]

    # ambiguous segments
    bad_segment_to_neighbors = defaultdict(int)
    for pattern in patterns:
        for segment in pattern:
            bad_segment_to_neighbors[segment] += len(pattern) - 1

    segments_used = set(bad_segment_to_segment.values())
    for bad_segments in freq_to_bad_segments.values():
        for bad_segment in bad_segments:
            bad_segment_neighbors = bad_segment_to_neighbors[bad_segment]
            candidates = neighbors_to_segments[bad_segment_neighbors]
            segment = next(iter(candidates - segments_used), None)
            bad_segment_to_segment[bad_segment] = segment
            segments_used.add(segment)

    return bad_segment_to_segment


def transform_segments(displayed_num: str, bad_segment_to_segment: dict[str, str]) -> str:
    trasnformed = []
    for bad_segment in displayed_num:
        trasnformed.append(bad_segment_to_segment[bad_segment])
    return ''.join(sorted(trasnformed))


def calc_number(
        displayed_nums: list[str], bad_segment_to_segment: dict[str, str], segment_to_num: dict[str, int]
) -> int:
    number = 0
    for displayed_num in displayed_nums:
        displayed_num = transform_segments(displayed_num, bad_segment_to_segment)
        displayed_num = segment_to_num[displayed_num]
        number = (number * 10) + displayed_num
    return number


def solve_displays(
        patterns_displayed_pairs: list[tuple[list[str], list[str]]],
        segment_to_num: dict[str, int],
        freq_to_segments: dict[int, set[str]],
        neighbors_to_segments: dict[int, set[str]]
) -> list[int]:
    numbers = []
    for patterns, displayed_nums in patterns_displayed_pairs:
        bad_segment_to_segment = solve_display(patterns, freq_to_segments, neighbors_to_segments)
        number = calc_number(displayed_nums, bad_segment_to_segment, segment_to_num)
        numbers.append(number)
    return numbers


if __name__ == '__main__':

    patterns_displayed_pairs = read_input('input.txt')

    num_to_segments = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg'
    }

    segment_to_freq = defaultdict(int)
    segment_to_neighbors = defaultdict(int)
    for segments in num_to_segments.values():
        for segment in segments:
            segment_to_freq[segment] += 1
            segment_to_neighbors[segment] += len(segments) - 1
    freq_to_segments = invert_dict(segment_to_freq)
    neighbors_to_segments = invert_dict(segment_to_neighbors)
    segment_to_num = {segments: num for num, segments in num_to_segments.items()}

    numbers = solve_displays(patterns_displayed_pairs, segment_to_num, freq_to_segments, neighbors_to_segments)
    print(sum(numbers))
