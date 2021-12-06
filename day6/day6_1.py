from collections import deque


def fishes_after_N_days(fish_timers: [int], days: int) -> int:
    timer_start_day_pairs = deque([(timer, 0) for timer in fish_timers])
    fishes = len(fish_timers)
    while timer_start_day_pairs:
        timer, start_day = timer_start_day_pairs.popleft()
        if (next_day := (start_day + timer + 1)) <= days:
            timer_start_day_pairs.append((8, next_day))
            fishes += 1
        while (next_day := (next_day + 7)) <= days:
            timer_start_day_pairs.append((8, next_day))
            fishes += 1
    return fishes


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        fish_timers = [int(n) for n in fp.read().strip().split(',')]

    print(fishes_after_N_days(fish_timers, 80))
