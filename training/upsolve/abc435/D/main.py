#!/usr/bin/env python3
import sys
from atcoder import dsu
from bisect import bisect_left
from collections import defaultdict
from collections import deque
# import pypyjit
# pypyjit.set_param(inlining=0)     # or pypyjit.set_param('max_unroll_recursion=-1')

sys.setrecursionlimit(10 ** 6)

INF = 2 ** 64 - 1


def main():
    N, M = map(int, input().split())
    r_edge = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(lambda x: int(x) - 1, input().split())
        r_edge[y].append(x)
    Q = int(input())

    flg_map = [False] * N

    def update(init_v):
        nonlocal flg_map

        if flg_map[init_v]:
            return

        que = deque()
        que.append(init_v)
        flg_map[init_v] = True

        while que:
            v = que.popleft()
            for nv in r_edge[v]:
                if flg_map[nv]:
                    continue
                flg_map[nv] = True
                que.append(nv)

    def solve():
        f, v = map(int, input().split())
        v -= 1
        if f == 1:
            update(v)
        else:
            if flg_map[v]:
                print("Yes")
            else:
                print("No")
    
    for _ in range(Q):
        solve()


if __name__ == '__main__':
    main()
