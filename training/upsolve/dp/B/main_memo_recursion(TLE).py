#import sys
#sys.setrecursionlimit(10 ** 6)

N, K = map(int, input().split())
h_list = list(map(int, input().split()))

INF = float("Inf")

memo = [INF] * N

def dp(i):
    if memo[i] != INF: return memo[i]

    if i == 0:
        memo[i] = 0
        return memo[i]

    for k in range(1, K + 1):
        j = i - k
        if j >= 0:
            memo[i] = min(memo[i], dp(j) + abs(h_list[i] - h_list[j]))
    return memo[i]

print(dp(N - 1))