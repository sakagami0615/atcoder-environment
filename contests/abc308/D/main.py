#!/usr/bin/env python3
import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

MOD = 5  # type: int
YES = "Yes"  # type: str
NO = "No"  # type: str
INF = float('inf')  # type: float


H, W = map(int, input().split())
S = [input() for _ in range(H)]


TEMP = "snuke"
MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]


visited = [[False] * W for _ in range(H)]

def dfs(x, y, cnt):
    global visited
    if y == H - 1 and x == W - 1:
        print(YES)
        exit()

    visited[y][x] = True
    for m in MOVE:
        nx, ny = x + m[0], y + m[1]
        nc = (cnt + 1) % MOD
        if nx < 0 or ny < 0 or nx >= W or ny >= H:
            continue

        if visited[ny][nx]:
            continue

        if S[ny][nx] == TEMP[nc]:
            dfs(nx, ny, nc)

dfs(0, 0, 0)
print(NO)