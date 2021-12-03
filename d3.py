def part1(nums, bit_len):
    z_list = [0 for x in range(bit_len)]
    for n in nums:
        dig = [int(x) for x in n]
        # print(dig)
        for i in range(len(dig)):
            if dig[i] == 0:
                z_list[i] += 1
            else:
                z_list[i] -= 1

    print(z_list)
    gama = ''
    ep = ''
    for z in z_list:
        if z > 0:
            gama += '0'
            ep += '1'
        else:
            gama += '1'
            ep += '0'

    print(gama)
    print(ep)
    g = int(gama, 2)
    e = int(ep, 2)

    p = g * e
    print(p)


def part2(nums, bit_len):
    bit_index = 0
    bit_index_c = 0
    ox_list, co_list = get_next_bit_nums_lists(bit_index, nums)

    # print(ox_list)
    # print(co_list)

    while len(ox_list) > 1 and len(co_list) > 1 and bit_index < bit_len - 1:
        bit_index += 1
        ox_list, c_list = get_next_bit_nums_lists(bit_index, ox_list)

    while len(co_list) > 1 and bit_index_c < bit_len - 1:
        bit_index_c += 1
        o_list, co_list = get_next_bit_nums_lists(bit_index_c, co_list)


    print('ox list {}'.format(ox_list))
    print('co list {}'.format(co_list))

    o = int(ox_list[0], 2)
    c = int(co_list[0], 2)

    s = o * c
    print(s)


def get_next_bit_nums_lists(bit_index, nums_list):
    # print('bit index {}'.format(bit_index))
    oxy_list = []
    co2_list = []
    zero_list = []
    one_list = []
    for n in nums_list:
        dig = [int(x) for x in n]
        # print(dig)
        if dig[bit_index] == 0:
            zero_list.append(n)
        else:
            one_list.append(n)

    if len(zero_list) > len(one_list):
        oxy_list = zero_list
        co2_list = one_list
    else:  # should take care of equal len also
        oxy_list = one_list
        co2_list = zero_list

    return oxy_list, co2_list


def main():
    numbers = []

    with open('d3.txt') as f:
        for line in f:
            numbers.append(line.rstrip())

    dig = [int(x) for x in numbers[0]]
    b_len = len(dig)
    # print(numbers)
    part1(numbers, b_len)
    part2(numbers, b_len)

if __name__ == '__main__':
    main()
