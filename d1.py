def find_increase_part1(nums):
    cnt = 0
    inc = 0
    pre = 0
    for n in nums:
        cnt += 1

        if cnt > 1:
            if n - pre > 0:
                inc += 1
        pre = n

    return inc


def get_all_sums(nums):
    sums = []
    cnt = 0
    for n in nums:
        if cnt + 2 < len(nums):
            sum = n + nums[cnt + 1] + nums[cnt + 2]
            # print(sum)
            sums.append(sum)
            cnt += 1
    return sums


def find_increase_part2(nums):
    sums = get_all_sums(nums)
#    print(sums)
    return find_increase_part1(sums)


def main():
    numbers = []

    with open('d1.txt') as f:
        for line in f:
            numbers.append(int(line.rstrip()))

    m = find_increase_part1(numbers)  
    print(m)
    m = find_increase_part2(numbers)
    print(m)


if __name__ == '__main__':
    main()
