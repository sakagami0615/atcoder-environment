import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

a_list = [list(map(int, input().split())) for _ in range(N)]

memo = [[0] * 3 for _ in range(N)]

def dp(i, p):
    if memo[i][p] != 0: return memo[i][p]

    if i == 0:
        memo[0][p] = a_list[0][p]
        return memo[0][p]

    for k in range(3):
        if p == k: continue
        memo[i][p] = max(memo[i][p], dp(i - 1, k) + a_list[i][p])
    return memo[i][p]

ans = 0
for p in range(3):
    ans = max(ans, dp(N - 1, p))
print(ans)
