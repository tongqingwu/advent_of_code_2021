import re
import collections


def get_dict(inputs, boards):
    d = dict()
    for b in boards:
        input_cnt_new, new_b = find_input_cnt_board(inputs, b)
        d[input_cnt_new] = new_b
    return d


def get_result(inputs, input_cnt, small_b):
    last_input = inputs[input_cnt - 1]
    print('last input {}, b {}, cnt {}'.format(last_input, small_b, input_cnt))
    sum = 0
    for r in small_b:
        for n in r:
            if n != -1:
                sum += n
    print(sum * last_input)


# return cnt of input for any row is empty for each board and new b, and last input
def find_input_cnt_board(inputs, b):
    n_b = b.copy()
    input_cnt = 0
    for i in inputs:
        input_cnt += 1
        for r in range(5):
            for c in range(5):
                if b[r][c] == i:
                    n_b[r][c] = -1
                    if check_row_col(n_b):
                        print('Find input cnt {} and last input {} for b {}'.format(input_cnt, i, b))
                        return input_cnt, n_b


def check_row_col(b):
    for r in range(5):
        if b[r][0] == b[r][1] == b[r][2] == b[r][3] == b[r][4] == -1 or b[0][r] == b[1][r] == b[2][r] == b[3][r] == b[4][r] == -1:
            return True


def main():
    board = [] # one board
    boards = []   # two dimension arrays.
    inputs = []
    cnt = 0
    board = []
    r_cnt = 0
    with open('d4.txt') as f:
        for line in f:
            line = line.rstrip()
            cnt += 1
            if cnt == 1:
                inputs_strs = line.split(',')
                inputs = [int(x) for x in inputs_strs]
                print(inputs)
            else:
                if line != '':
                    row = re.findall(r'\S+', line)
                    board.append([int(x) for x in row])
                    r_cnt += 1

                    if r_cnt == 5:
                        boards.append(board)
                        board = []
                        r_cnt = 0

    # print(inputs)
    # print(boards)

    d = get_dict(inputs, boards)
    od = collections.OrderedDict(sorted(d.items()))

    items = list(od.items())

    p1 = items[0]
    get_result(inputs, p1[0], p1[1])

    p2 = items[len(items) - 1]
    get_result(inputs, p2[0], p2[1])


if __name__ == '__main__':
    main()
