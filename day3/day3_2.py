def count_ones_by_position(binary_codes, start, end, longest_bc):
    one_counter_by_position = [0 for _ in range(end - start)]
    for bc in binary_codes:
        offset = len(longest_bc) - len(bc)
        for idx in range(start, min(len(bc), end)):
            one_counter_by_position[offset + idx - start] += int(bc[idx])
    return one_counter_by_position


def search_oxygen_generator_rating(binary_codes, longest_bc):
    for idx in range(len(longest_bc)):
        limit = (len(binary_codes) // 2) + (0 if len(binary_codes) % 2 else -1)
        one_counter_by_position = count_ones_by_position(binary_codes, idx, idx+1, longest_bc)
        bit_required = ''.join('1' if pos_count > limit else '0' for pos_count in one_counter_by_position)
        binary_codes = list(filter(lambda bc: bc[idx] == bit_required, binary_codes))
        if len(binary_codes) == 1:
            break
    return int(binary_codes[0], 2)


def search_co2_scrubber_rating(binary_codes, longest_bc):
    for idx in range(len(longest_bc)):
        limit = (len(binary_codes) // 2) + (0 if len(binary_codes) % 2 else -1)
        one_counter_by_position = count_ones_by_position(binary_codes, idx, idx+1, longest_bc)
        bit_required = ''.join('0' if pos_count > limit else '1' for pos_count in one_counter_by_position)
        binary_codes = list(filter(lambda bc: bc[idx] == bit_required, binary_codes))
        if len(binary_codes) == 1:
            break
    return int(binary_codes[0], 2)


if __name__ == '__main__':

    with open('input.txt', 'r') as fp:
        binary_codes = [bc.strip() for bc in fp.readlines()]

    longest_bc = max(binary_codes, key=len)
    oxygen_generator_rating = search_oxygen_generator_rating(binary_codes, longest_bc)
    co2_scrubber_rating = search_co2_scrubber_rating(binary_codes, longest_bc)
    ans = oxygen_generator_rating * co2_scrubber_rating
    print(ans)

