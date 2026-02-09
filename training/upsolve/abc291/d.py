MOD = 998244353

N = int(input())

ab_list = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 2 for _ in range(N)]
dp[0][0] = dp[0][1] = 1

for i in range(1, N):
    for j in range(2):
        for k in range(2):
            if ab_list[i][j] != ab_list[i - 1][k]:
                dp[i][j] += dp[i - 1][k]
                dp[i][j] %= MOD


print(sum(dp[-1]) % MOD)
