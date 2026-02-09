
A, B, C, D, E, F, X = map(int, input().split())

def calc(a, b, c, x):

    div = x // (a + c)
    mod = x % (a + c)

    ret = div * a * b
    if mod != 0:
        ret += b * min(a, mod)
    return ret

taka_ans = calc(A, B, C, X)
aoki_ans = calc(D, E, F, X)


if taka_ans > aoki_ans:
    print("Takahashi")
elif taka_ans < aoki_ans:
    print("Aoki")
else:
    print("Draw")
