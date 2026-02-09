
def cvt_abcd(h, m):
    return h // 10, h % 10, m // 10, m % 10

def cvt_hm(a, b, c, d):
    return a * 10 + b, c * 10 + d


def add_m(h, m, add_m):

    ret_h, ret_m = h, m
    ret_m += add_m

    if ret_m >= 60:
        add_h = ret_m // 60
        ret_m %= 60
        ret_h += add_h

        if ret_h >= 24:
            ret_h %= 24

    return ret_h, ret_m


def judge(h, m):
    a, b, c, d = cvt_abcd(h, m)
    h, m = cvt_hm(a, c, b, d)
    ret = False
    if 0 <= h < 24 and 0 <= m < 60:
        ret = True
    return ret


H, M = map(int, input().split())

curr_h, curr_m = H, M

while True:
    ret = judge(curr_h, curr_m)
    if ret:
        break

    curr_h, curr_m = add_m(curr_h, curr_m, 1)

print(*[curr_h, curr_m])
