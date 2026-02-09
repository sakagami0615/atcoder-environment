N = int(input())
C, P = [], [[] for _ in range(N)]
for i in range(N):
  l = list(map(int, input().split()))
  C.append(l[0])
  for p in l[1:]:
    P[i].append(p - 1)

edges = [[] for _ in range(N)]
for i, ps in enumerate(P):
  for p in ps:
    edges[i].append(p)

visited = [False] * N
data = []
for v in edges[0]:
  data.append(v)
  visited[v] = True

ans = []
while data:
  cur = data[-1]

  cnt = 0
  for nxt in edges[cur]:
    if visited[nxt]: continue
    data.append(nxt)
    visited[nxt] = True
    cnt += 1
  if cnt == 0:
    ans.append(data.pop() + 1)

print(*ans)
