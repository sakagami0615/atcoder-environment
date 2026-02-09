n, m = map(int, input().split())

graph = [[] for _ in  range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    graph[a].append(b + 1)
    graph[b].append(a + 1)

for i in range(n):
    graph[i].sort()

for node in graph:
    ans = [len(node)] + node
    print(*ans)
