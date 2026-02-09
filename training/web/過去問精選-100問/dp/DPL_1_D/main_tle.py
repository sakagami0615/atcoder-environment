
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=ja
# Result -> TLE: https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7296597#2

INF = float("INF")

N = int(input())
A = [int(input()) for _ in range(N)]

dp = [INF] * N
dp[0] = 1

for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
