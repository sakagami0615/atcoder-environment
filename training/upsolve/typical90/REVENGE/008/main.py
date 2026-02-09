
MOD = 1000000007

N = int(input())
S = input()

l = 'atcoder#'
n_l = len(l)

dp = [[0] * n_l for _ in range(N + 1)]

dp[0][0] = 1

for i in range(N):
    for j in range(n_l):
        dp[i + 1][j] += dp[i][j]
        dp[i + 1][j] %= MOD
        if S[i] == l[j]:
            dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] %= MOD

#for a in dp:
#    print(a)

print(dp[-1][-1])