import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
h_list = list(map(int, input().split()))

INF = float("Inf")

memo = [INF] * N

def dp(i):

    if memo[i] != INF:
        return memo[i]

    if i == 0:
        memo[0] = 0
        return memo[0]

    memo[i] = dp(i - 1) + abs(h_list[i] - h_list[i - 1])
    if i >= 2:
        memo[i] = min(memo[i], dp(i - 2) + abs(h_list[i] - h_list[i - 2]))
    return memo[i]

print(dp(N - 1))
