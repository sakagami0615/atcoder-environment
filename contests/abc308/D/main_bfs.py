#!/usr/bin/env python3
import sys
from collections import defaultdict, deque


MOD = 5  # type: int
YES = "Yes"  # type: str
NO = "No"  # type: str
INF = float('inf')  # type: float


H, W = map(int, input().split())
S = [input() for _ in range(H)]


TEMP = "snuke"
MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]


visited = [[False] * W for _ in range(H)]


que = deque()
que.append((0, 0, 0))
visited[0][0] = True

while que:
    x, y, c = que.popleft()

    if x == W - 1 and y == H - 1:
        print(YES)
        exit()

    for m in MOVE:
        nx, ny, nc = x + m[0], y + m[1], (c + 1) % MOD

        if nx < 0 or ny < 0 or nx >= W or ny >= H:
            continue
        if visited[ny][nx]:
            continue

        if S[ny][nx] == TEMP[nc]:
            visited[ny][nx] = True
            que.append((nx, ny, nc))

print(NO)
