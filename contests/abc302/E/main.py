
N, Q = map(int, input().split())

query = [list(map(int, input().split())) for _ in range(Q)]

edges = [set() for _ in range(N)]
counts = [0] * N

ans_set = set([i for i in range(N)])

for q in query:
    if q[0] == 1:
        u, v = q[1] - 1, q[2] - 1
        edges[u].add(v)
        edges[v].add(u)
        if counts[u] == 0: ans_set.remove(u)
        if counts[v] == 0: ans_set.remove(v)
        counts[u] += 1
        counts[v] += 1

    else:
        v = q[1] - 1
        for u in edges[v]:
            edges[u].remove(v)
            counts[u] -= 1
            if counts[u] == 0:
                ans_set.add(u)
        edges[v] = set()
        counts[v] = 0
        ans_set.add(v)

    print(len(ans_set))

