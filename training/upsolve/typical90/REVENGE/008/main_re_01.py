"""
S = "attcordeer"
T = "atcoder"

dp = [{N + 1}][{len(T) + 1}]
    0 1 2 3 4 5 6 7 8 9 10
    a t t c o r d e e r *
  +-----------------------
a |[1]1 1 1 1 1 1 1 1 1 1
t | 0 1 1 1 1 1 1 1 1 1 1
c | 0 0 1 2 2 2 2 2 2 2 2
o | 0 0 0 0 2 2 2 2 2 2 2
d | 0 0 0 0 0 2 2 2 2 2 2
e | 0 0 0 0 0 0 0 2 2 2 2
r | 0 0 0 0 0 0 0 0 2 4 4
* | 0 0 0 0 0 0 0 0 0 0 4

update: →
add: ↘
"""

MOD = 10 ** 9 + 7

N = int(input())
S = input()
T = "atcoder*"
n_t = len(T)
dp = [[0] * n_t for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(n_t):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        if S[i] == T[j]:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

print(dp[N][n_t - 1])