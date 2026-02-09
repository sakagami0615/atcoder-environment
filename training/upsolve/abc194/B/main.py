N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

ans = float("INF")
for a, b in AB:
    ans = min(ans, a + b)

for i in range(N):
    for j in range(N):
        if i != j:
            t = max(AB[i][0], AB[j][1])
            ans = min(ans, t)

print(ans)
