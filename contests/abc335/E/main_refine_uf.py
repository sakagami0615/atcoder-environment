from atcoder.dsu import DSU

N, M = map(int, input().split())

A = list(map(int, input().split()))
UV = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

comp_a = {a: i for i, a in enumerate(sorted(set(A)))}

edges = [[] for _ in range(N)]
uf = DSU(N)
for u, v in UV:
    if A[u] > A[v]:
        u, v = v, u
    if A[u] == A[v]:
        uf.merge(u, v)
    else:
        edges[comp_a[A[u]]].append((u, v))

dp = [0] * N
dp[uf.leader(0)] = 1

for a in edges:
    for u, v in a:
        u = uf.leader(u)
        v = uf.leader(v)
        if dp[u] > 0:
            dp[v] = max(dp[v], dp[u] + 1)

print(dp[uf.leader(N - 1)])
