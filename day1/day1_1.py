if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        prev = None
        count = 0
        for depth in map(int, fp.readlines()):
            if prev is not None:
                count += 1 if depth > prev else 0
            prev = depth
    print(count)
