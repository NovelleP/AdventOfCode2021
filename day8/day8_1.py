def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as fp:
        displayed_nums = [e for line in fp.readlines() for e in line.split('|')[1].strip().split()]
    return displayed_nums


if __name__ == '__main__':

    displayed_nums = read_input('input.txt')

    target_lengths = {2, 4, 3, 7}
    ans = len([e for e in displayed_nums if len(e) in target_lengths])
    print(ans)
