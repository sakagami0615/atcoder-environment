#!/usr/bin/env python3
# import sys
# from atcoder import dsu
# from bisect import bisect_left
# from collections import defaultdict
# from collections import deque
# import pypyjit
# pypyjit.set_param(inlining=0)     # or pypyjit.set_param('max_unroll_recursion=-1')

# sys.setrecursionlimit(10 ** 6)

INF = 2 ** 64 - 1

def solve():
    N, M = map(int, input().split())
    C, A = [], []
    for _ in range(M):
        c = int(input())
        a = set(list(map(int, input().split())))
        C.append(c)
        A.append(a)
    
    def check(store):
        for i in range(1, N + 1):
            if i not in store:
                return False
        return True

    cnt = 0
    bit_max = M
    for bit in range(2 ** bit_max):     
        store = set()
        for idx in range(bit_max):
            if bit & (1 << idx):
                store |= A[idx]
        
        if check(store):
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    solve()
