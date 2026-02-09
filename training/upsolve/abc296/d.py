"""
M = 7, N = 5
a, b = {1 2 3 4 5}
X = a * b (a * b >= M)
(X = a ^ 2)

:cond
a >= √M (a <= N)

-----
a * b >= M
b >= M / a
(M / a <= N)

a = loop (1 <= a <= N)
b = ceil(M / a)

:ans-cond
1 <= b <= N
"""

from math import ceil

N, M = map(int, input().split())

if N * N < M:
    print(-1)
    exit()


ans = float("INF")
for a in range(1, N + 1):
    b = ceil(M / a)
    if 1 <= b <= N:
        ans = min(ans, a * b)
    if a > b:
        break

if ans == float("INF"):
    print(-1)
else:
    print(ans)
