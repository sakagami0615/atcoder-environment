#!/usr/bin/env python3
import sys
from collections import defaultdict


NO = "Impossible"  # type: str
INF = float('inf')  # type: float

N = int(input())
A = list(map(int, input().split()))

costs = [[0] * N for _ in range(N)]
dists = [[INF] * N for _ in range(N)]
for i in range(N):
    S = input()
    for j in range(N):
        if i == j:
            dists[i][j] = 0
        elif S[j] == "Y":
            costs[i][j] = A[j]
            dists[i][j] = 1

# warshall_floyd
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist = dists[i][k] + dists[k][j]
            if dists[i][j] > dist:
                dists[i][j] = dist
                costs[i][j] = costs[i][k] + costs[k][j]
            elif dists[i][j] == dist:
                dists[i][j] = dist
                costs[i][j] = max(costs[i][j], costs[i][k] + costs[k][j])

Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if dists[u][v] == INF:
        print(NO)
    else:
        print(dists[u][v], costs[u][v] + A[u])
