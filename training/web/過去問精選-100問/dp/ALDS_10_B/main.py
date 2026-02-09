# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_B

INF = float("Inf")

N = int(input())
R = [list(map(int, input().split())) for _ in range(N)]


dp = [[0] * (N) for _ in range(N)]


# l: 切り取る長さ
# i: 切り取った範囲の先頭インデックス
# j: 切り取った範囲の末尾インデックス
# k: 切り取った範囲無の括弧の区切りインデックス
for l in range(2, N + 1):
    for i in range(N - l + 1):
        j = i + l - 1

        min_value = INF
        for k in range(i, j):
            value = dp[i][k] + dp[k + 1][j] + (R[i][0] * R[k][1] * R[j][1])
            if min_value > value:
                min_value = value

        dp[i][j] = min_value


print(dp[0][-1])

#for d in dp:
#    print(d)
