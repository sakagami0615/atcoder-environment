#!/usr/bin/env python3
import sys
# from atcoder import dsu
from bisect import bisect_left
# from collections import defaultdict
# from collections import deque
# import pypyjit
# pypyjit.set_param(inlining=0)     # or pypyjit.set_param('max_unroll_recursion=-1')

# sys.setrecursionlimit(10 ** 6)

# INF = 2 ** 64 - 1


def solve():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    BC = []
    for b in B:
        for c in C:
            BC.append(b + c)
    
    N_BC = len(BC)
    BC.sort()

    # おいしさ(delicious)以上のパターン数がK以上あるかどうか
    def check(delicious):
        cnt = 0
        for a in A:
            idx = bisect_left(BC, delicious - a)
            cnt += N_BC - idx
            if cnt >= K:
                break
        return cnt >= K

    head, tail = 0, 10000000000 * 4
    while head + 1 < tail:
        mid = (head + tail) // 2
        if check(mid):
            head = mid
        else:
            tail = mid
    
    BC = BC[::-1]

    ans = []
    for a in A:
        for bc in BC:
            s = a + bc
            if head < s:
                ans.append(s)
            else:
                break
    while len(ans) < K:
        ans.append(head)

    ans.sort(reverse=True)
    for a in ans[:K]:
        print(a)
    
if __name__ == "__main__":
    solve()
