#!/usr/bin/env python3
import sys
from collections import deque


def iterate_tokens():
    for line in sys.stdin:
        for word in line.split():
            yield word
tokens = iterate_tokens()
N = int(next(tokens))  # type: int
M = int(next(tokens))  # type: int
u = [int()] * (M)  # type: "List[int]"
v = [int()] * (M)  # type: "List[int]"
for i in range(M):
    u[i] = int(next(tokens))
    v[i] = int(next(tokens))

edges = [[] for _ in range(N)]
for _u, _v in zip(u, v):
    _u -= 1
    _v -= 1
    edges[_u].append(_v)
    edges[_v].append(_u)

pt_color = [None] * N



def bfs(bi):
    que = deque()
    que.append((bi, 1))
    pt_color[bi] = 1
    n_b = 1
    n_w = 0
    while que:
        curr, color = que.popleft()

        for next in edges[curr]:
            if pt_color[next] is None:
                que.append((next, -color))
                pt_color[next] = -color
                if -color == 1:
                    n_b += 1
                else:
                    n_w += 1

            elif pt_color[next] == color:
                return -1, -1

    return n_b, n_w


# solve
ans = N * (N - 1) / 2 - M
for i in range(N):
    if pt_color[i] is not None:
        continue

    n_b, n_w = bfs(i)
    if n_b == -1:
        print(0)
        sys.exit()

    ans -= n_b * (n_b - 1) / 2
    ans -= n_w * (n_w - 1) / 2

print(int(ans))