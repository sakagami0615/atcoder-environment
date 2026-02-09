import sys
from collections import defaultdict
from collections import deque


N, M = map(int, input().split())

graph = [set() for _ in range(N)]
edge_count = defaultdict(int)

key = lambda a, b: (min(a, b), max(a, b))

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].add(v)
    graph[v].add(u)
    edge_count[key(u, v)] += 1

visit = [False] * N

for i in range(N):
    if visit[i] == True:
        continue

    que = deque()
    que.append(i)
    visit[i] = True

    n_node, n_edge = 0, 0
    while que:
        c = que.popleft()

        n_node += 1

        for n in graph[c]:
            if edge_count[key(c, n)] == 0:
                continue
            n_edge += edge_count[key(c, n)]
            edge_count[key(c, n)] = 0

            if visit[n]:
                continue
            visit[n] = True
            que.append(n)

    if n_node != n_edge:
        print("No")
        sys.exit()

print("Yes")
