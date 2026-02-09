# https://atcoder.jp/contests/abc032/tasks/abc032_c
# https://nashidos.hatenablog.com/entry/2020/02/02/165319

import sys

N, K = map(int, input().split())
s_n = [int(input()) for _ in range(N)]


if 0 in s_n:
    print(N)
    sys.exit()


ans = 0
r, value = 0, 1

for l in range(N):

    while r < N and value * s_n[r] <= K:
        value *= s_n[r]
        r += 1

    print((l, r))

    ans = max(ans, r - l)
    if l == r:
        r += 1
    else:
        value /= s_n[l]

print(ans)
