from bisect import bisect_left, bisect_right
from collections import defaultdict


H, W, sr, sc = map(int, input().split())
N = int(input())


h_wall_dict = defaultdict(list)
w_wall_dict = defaultdict(list)
for _ in range(N):
    r, c = map(int, input().split())
    h_wall_dict[c].append(r)
    w_wall_dict[r].append(c)

for k in h_wall_dict.keys():
    h_wall_dict[k].sort()
for k in w_wall_dict.keys():
    w_wall_dict[k].sort()


Q = int(input())
q_list = [list(input().split()) for _ in range(Q)]


for q in q_list:
    K, V = q
    V = int(V)
    if K == "U":
        limit = 1
        if h_wall_dict[sc]:
            idx = bisect_left(h_wall_dict[sc], sr)
            if idx > 0:
                limit = h_wall_dict[sc][idx - 1] + 1
        sr = max(limit, sr - V)

    elif K == "D":
        limit = H
        if h_wall_dict[sc]:
            idx = bisect_right(h_wall_dict[sc], sr)
            if idx < len(h_wall_dict[sc]):
                limit = h_wall_dict[sc][idx] - 1
        sr = min(limit, sr + V)

    elif K == "L":
        limit = 1
        if w_wall_dict[sr]:
            idx = bisect_left(w_wall_dict[sr], sc)
            if idx > 0:
                limit = w_wall_dict[sr][idx - 1] + 1
        sc = max(limit, sc - V)

    else:
        limit = W
        if w_wall_dict[sr]:
            idx = bisect_right(w_wall_dict[sr], sc)
            if idx < len(w_wall_dict[sr]):
                limit = w_wall_dict[sr][idx] - 1
        sc = min(limit, sc + V)

    print(sr, sc)