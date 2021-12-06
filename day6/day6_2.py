memo = {}


def dfs(timer: int, start_day: int, end_day: int) -> int:
    if (timer, start_day) in memo:
        return memo[(timer, start_day)]
    elif (start_day + timer + 1) <= end_day:
        memo[(timer, start_day)] = 1 + dfs(6, start_day + timer + 1, end_day) + dfs(8, start_day + timer + 1, end_day)
    else:
        memo[(timer, start_day)] = 0
    return memo[(timer, start_day)]


def fishes_after_N_days(fish_timers: list[int], days: int) -> int:
    timers = [0 for _ in range(9)]
    for timer in fish_timers:
        timers[timer] += 1

    fishes = len(fish_timers)
    for timer, freq in enumerate(timers):
        fishes += freq * dfs(timer, 0, days)
    return fishes


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        fish_timers = [int(n) for n in fp.read().strip().split(',')]

    print(fishes_after_N_days(fish_timers, 256))
