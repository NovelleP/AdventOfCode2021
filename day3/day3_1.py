def count_ones_by_position(binary_codes):
    longest_bc = max(binary_codes, key=len)
    one_counter_by_position = [0 for _ in longest_bc]
    for bc in binary_codes:
        offset = len(longest_bc) - len(bc)
        for idx, bit in enumerate(bc):
            one_counter_by_position[offset + idx] += int(bit)
    return one_counter_by_position


def calc_gamma(one_counter_by_position, size):
    limit = size // 2
    gamma_rate = ''.join('1' if pos_count > limit else '0' for pos_count in one_counter_by_position)
    return int(gamma_rate, 2)


def calc_epsilon(one_counter_by_position, size):
    limit = size // 2
    epsilon_rate = ''.join('0' if pos_count > limit else '1' for pos_count in one_counter_by_position)
    return int(epsilon_rate, 2)


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        binary_codes = [bc.strip() for bc in fp.readlines()]

    one_counter_by_position = count_ones_by_position(binary_codes)
    gamma_rate = calc_gamma(one_counter_by_position, len(binary_codes))
    epsilon_rate = calc_epsilon(one_counter_by_position, len(binary_codes))
    ans = gamma_rate * epsilon_rate

