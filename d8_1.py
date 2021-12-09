
s1 = {'cf'}
s7 = {'cf', 'a'}
s4 = {'cf', 'bd'}
s8 = {'cf', 'bd', 'a', 'eg'}

s0 = {'a', 'cf', 'eg', 'b'}  # len 6, got b
s2 = {'a', 'eg', 'c', 'd'}
s3 = {'a', 'cf', 'd', 'g'}
s5 = {'a', 'bd', 'f', 'g'}
s6 = {'a', 'bd', 'eg', 'f'}  # len 6, got f
s9 = {'a', 'bd', 'cf', 'g'}  # len 6, got g


def find_codes(inps, outs):
    print('new input ------------------------------ ')
    codes = []
    dict_code = dict()
    real_code = dict.fromkeys('abcdefg')
    tmp_5 = []
    tmp_6 = []
    for i in inps:
        len_i = len(i)
        if len_i == 2:
            dict_code['cf'] = i

        if len_i == 3:
            dict_code['a'] = i.replace(dict_code['cf'][0], '').replace(dict_code['cf'][1], '')
            real_code['a'] = dict_code['a']

        if len_i == 4:
            tmp = i.replace(dict_code['cf'][0], '').replace(dict_code['cf'][1], '')
            if len(tmp) == 2:
                dict_code['bd'] = tmp

        if len_i == 5:
            tmp_5.append(i)

        if len_i == 6:
            tmp_6.append(i)

        if len_i == 7:
            tmp_6.append(i)
            tmp = i.replace(dict_code['bd'][0], '').replace(dict_code['bd'][1], '').replace(dict_code['cf'][0],
                                                                                            '').replace(
                dict_code['cf'][1], '').replace(real_code['a'], '')
            if len(tmp) == 2:
                dict_code['eg'] = tmp

    real_code['b'], real_code['f'], real_code['g'] = get_bfg(dict_code, tmp_6)

    # print('dict new: {}'.format(dict_code))

    while None in real_code.values():
        real_code = update_dict(real_code, dict_code, tmp_5)

    print('dict all: {}'.format(real_code))

    for o in outs:
        if len(o) == 2:
            t = o.replace(dict_code['cf'][0], '').replace(dict_code['cf'][1], '')
            if len(t) == 0:
                codes.append(o)

        if len(o) == 3:
            t = o.replace(dict_code['cf'][0], '').replace(dict_code['cf'][1], '').replace(dict_code['a'], '')
            if len(t) == 0:
                codes.append(o)

        if len(o) == 4:
            t = o.replace(dict_code['cf'][0], '').replace(dict_code['cf'][1], '').replace(dict_code['bd'][0],
                                                                                          '').replace(
                dict_code['bd'][1], '')
            if len(t) == 0:
                codes.append(o)

        # if len(o) == 5:
        #     print('t2')
        #     t2 = replace_digs(o, get_digs(s2), real_code)
        #     t3 = replace_digs(o, get_digs(s3), real_code)
        #     print('t5 -----------------------')
        #     t5 = replace_digs(o, get_digs(s5), real_code)
        #     
        #     print('t2 {}, t3 {}, t5 {}'.format(t2, t3, t5))
        #     if len(t2) == 0 or len(t3) == 0 or len(t5) == 0:
        #         codes.append(o)

        # if len(o) == 6:
        #     t0 = replace_digs(o, get_digs(s0), real_code)
        #     t6 = replace_digs(o, get_digs(s6), real_code)
        #     t9 = replace_digs(o, get_digs(s9), real_code)
        # 
        #     if len(t0) == 0 or len(t6) == 0 or len(t9) == 0:
        #         codes.append(o)

        if len(o) == 7:
            t8 = replace_digs(o, get_digs(s8), real_code)
            if len(t8) == 0:
                codes.append(o)

    print(codes)
    print(len(codes))
    return codes


def get_digs(input_set):
    all_s = ''
    for s in input_set:
        all_s += s

    return all_s


def replace_digs(inp, digs, real_code):
    # print('inp {} and dig {}'.format(inp, digs))
    for d in digs:
        # print(real_code)
        # print('{} -> {}'.format(d, real_code[d]))
        inp = inp.replace(real_code[d], '')

    # print('new: {}'.format(new_in))
    return inp


def update_dict(real_code, dict_code, tmp_5):
    if real_code['b']:
        real_code['d'] = dict_code['bd'].replace(real_code['b'], '')
        c = get_c(real_code, dict_code, tmp_5)
        real_code['c'] = c
        if not real_code['g']:
            real_code['g'] = get_g_by_d(real_code, dict_code, tmp_5)

    if real_code['f']:
        real_code['c'] = dict_code['cf'].replace(real_code['f'], '')
        if not real_code['g']:
            real_code['g'] = get_g_by_f(real_code, dict_code, tmp_5)

    if real_code['g']:
        real_code['e'] = dict_code['eg'].replace(real_code['g'], '')
        if not real_code['f']:
            real_code['f'] = get_f_by_g(real_code, dict_code, tmp_5)
        if not real_code['d']:
            real_code['d'] = get_d_by_g(real_code, dict_code, tmp_5)

    if real_code['e']:
        if not real_code['g']:
            real_code['g'] = dict_code['eg'].replace(real_code['e'], '')

    if real_code['c']:
        if not real_code['f']:
            real_code['f'] = dict_code['cf'].replace(real_code['c'], '')

    if real_code['d']:
        if not real_code['b']:
            real_code['b'] = dict_code['bd'].replace(real_code['d'], '')

    return real_code


# in 2:
def get_c(real_code, dict_code, tmp5):
    c = ''
    for i in tmp5:
        cc = i.replace(dict_code['a'], '').replace(dict_code['eg'][0], '').replace(dict_code['eg'][1], '').replace(
            real_code['d'], '')
        if c == '' and len(cc) == 1:
            return cc


# in 3:
def get_g_by_d(real_code, dict_code, tmp5):
    g = ''
    for i in tmp5:
        gg = i.replace(dict_code['a'], '').replace(dict_code['cf'][0], '').replace(dict_code['cf'][1], '').replace(
            real_code['d'], '')
        if g == '' and len(gg) == 1:
            return gg


# in 3:
def get_d_by_g(real_code, dict_code, tmp5):
    d = ''
    for i in tmp5:
        dd = i.replace(real_code['a'], '').replace(dict_code['cf'][0], '').replace(dict_code['cf'][1], '').replace(
            real_code['g'], '')
        if d == '' and len(dd) == 1:
            return dd


# in 5:
def get_g_by_f(real_code, dict_code, tmp5):
    g = ''
    for i in tmp5:
        gg = i.replace(real_code['a'], '').replace(dict_code['bd'][0], '').replace(dict_code['bd'][1], '').replace(
            real_code['f'], '')
        if g == '' and len(gg) == 1:
            return gg


# in 5:
def get_f_by_g(real_code, dict_code, tmp5):
    f = ''
    for i in tmp5:
        ff = i.replace(real_code['a'], '').replace(dict_code['bd'][0], '').replace(dict_code['bd'][1], '').replace(
            real_code['g'], '')
        if f == '' and len(ff) == 1:
            return ff


def get_bfg(dict_code, tmp6):
    b = f = g = None
    for i in tmp6:
        bb = i.replace(dict_code['eg'][0], '').replace(dict_code['eg'][1], '').replace(dict_code['cf'][0], '').replace(
            dict_code['cf'][1], '').replace(dict_code['a'], '')
        ff = i.replace(dict_code['bd'][0], '').replace(dict_code['bd'][1], '').replace(dict_code['eg'][0], '').replace(
            dict_code['eg'][1], '').replace(dict_code['a'], '')
        gg = i.replace(dict_code['bd'][0], '').replace(dict_code['bd'][1], '').replace(dict_code['cf'][0], '').replace(
            dict_code['cf'][1], '').replace(dict_code['a'], '')

        if len(bb) == 1 and b is None:
            b = bb
        if len(ff) == 1 and f is None:
            f = ff
        if len(gg) == 1 and g is None:
            g = gg

    return b, f, g


def main():
    codes = []
    with open('d8.txt') as f:
        for line in f:
            line = line.rstrip()
            (inp, out) = line.split('|')
            inps = inp.split(' ')
            outs = out.split(' ')
            inps.remove('')
            outs.remove('')
            inps = sorted(inps, key=len)
            # print(inps)
            codes += find_codes(inps, outs)
    print(len(codes))


if __name__ == '__main__':
    main()

