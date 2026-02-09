from collections import deque
from heapq import heappop, heappush

N, M, K = map(int, input().split())

uva_list = [list(map(int, input().split())) for _ in range(M)]

edges = [[[] for _ in range(N)] for _ in range(2)]

for u, v, a in uva_list:
    u -= 1
    v -= 1
    status = 1 - a
    edges[status][u].append((v, 1, status))
    edges[status][v].append((u, 1, status))

for s in list(map(int, input().split())):
    s -= 1
    edges[0][s].append((s, 0, 1))
    edges[1][s].append((s, 0, 0))

# 0: pos, 1: status, 2: step
que = deque()
que.append((0, 0, 0))


dist = [[float('Inf')] * N for _ in range(2)]
used = [[False] * N for _ in range(2)]

dist[0][0] = 0
used[0][0] = True
queue = [(0, 0, 0)]

while queue:
    d, now, status = heappop(queue)
    used[status][now] = True
    for nxt, cost, nxt_status in edges[status][now]:
        if (not used[nxt_status][nxt]) and (dist[status][now] + cost < dist[nxt_status][nxt]):
            dist[nxt_status][nxt] = dist[status][now] + cost
            heappush(queue, (dist[nxt_status][nxt], nxt, nxt_status))

ans = min(dist[0][-1], dist[1][-1])

if ans == float("inf"):
    print(-1)
else:
    print(ans)
