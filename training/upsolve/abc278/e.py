
H, W, N, h, w = map(int, input().split())

INF = float("INF")

min_x = [INF] * (N)
min_y = [INF] * (N)
max_x = [0] * (N)
max_y = [0] * (N)

for hi in range(H):
    for wi, v in enumerate(map(int, input().split())):
        v -= 1
        min_x[v] = min(min_x[v], wi)
        min_y[v] = min(min_y[v], hi)
        max_x[v] = max(max_x[v], wi)
        max_y[v] = max(max_y[v], hi)


for hi in range(H - h + 1):
    ans_list = []
    for wi in range(W - w + 1):
        cnt = N
        for i in range(N):
            if (wi <= min_x[i] and wi + w > max_x[i] and
                hi <= min_y[i] and hi + h > max_y[i]):
                cnt -= 1
        ans_list.append(cnt)

    print(*ans_list)