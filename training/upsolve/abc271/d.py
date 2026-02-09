N, S = map(int, input().split())
ab_list = [list(map(int, input().split())) for _ in range(N)]


dp = [[False] * (S + 1) for _ in range(N + 1)]
dp[0][0] = True

for i, ab in enumerate(ab_list):
    for x in ab:
        for j in range(S + 1):
            if not dp[i][j]:
                continue

            if j + x <= S:
                dp[i + 1][j + x] = True

if dp[N][S] == 0:
    print("No")
    exit()

print("Yes")

ans = ""
idx = S
for i in range(N, 0, -1):
    a, b = ab_list[i - 1]
    if (idx - a) >= 0 and dp[i - 1][idx - a]:
        idx -= a
        ans += "H"
    else:
        idx -= b
        ans += "T"

ans = ans[::-1]
print(ans)

