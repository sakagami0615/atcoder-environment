from collections import deque

N, M, K = map(int, input().split())

uva_list = [list(map(int, input().split())) for _ in range(M)]

s_set = set()
for x in list(map(int, input().split())):
    s_set.add(x - 1)

edges = [[[] for _ in range(N)] for _ in range(2)]

for u, v, a in uva_list:
    u -= 1
    v -= 1
    status = 1 - a
    edges[status][u].append(v)
    edges[status][v].append(u)


# 0: pos, 1: status, 2: step
que = deque()
que.append((0, 0, 0))

dist = [[float("INF")] * N for _ in range(2)]
dist[0][0] = 0

while que:
    pos, status, step = que.popleft()

    for nxt_pos in edges[status][pos]:
        if dist[status][nxt_pos] <= step + 1:
            continue
        que.append((nxt_pos, status, step + 1))
        dist[status][nxt_pos] = step + 1
    if pos in s_set:
        if dist[1 - status][pos] <= step:
            continue
        que.append((pos, 1 - status, step))
        dist[1 - status][pos] = step

ans = min(dist[0][-1], dist[1][-1])

if ans == float("INF"):
    print(-1)
else:
    print(ans)
