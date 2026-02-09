# NOTE: TLEする

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
    
    A.sort(reverse=True)
    BC.sort(reverse=True)

    # おいしさ(delicious)以上のパターン数がK以上あるかどうか
    def check(delicious):
        cnt = 0
        for a in A:
            idx = bisect_left(BC, a - delicious)
            cnt += idx
        return cnt >= K

    
    head, tail = 0, 10000000000 * 4
    while head + 1 < tail:
        mid = (head + tail) // 2
#        print((head, tail), mid)
        if check(mid):
            head = mid
        else:
            tail = mid
#        print()

    delicious_thresh = head
    cands = []
    for a in A:
        for bc in BC:
            if a + bc < delicious_thresh:
                break
            cands.append(a + bc)
    cands.sort(reverse=True)
    for ans in cands[:K]:
        print(ans)
    
if __name__ == "__main__":
    solve()
