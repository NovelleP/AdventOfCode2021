if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        depths = list(map(int, fp.readlines()))

    count = 0
    sum_a = sum(depths[:3])
    for idx in range(3, len(depths)):
        sum_b = sum_a - depths[idx - 3] + depths[idx]
        count += 1 if sum_b > sum_a else 0

    print(count)
