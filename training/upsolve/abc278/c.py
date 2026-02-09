from collections import defaultdict

N, Q = map(int, input().split())

q_list = [list(map(int, input().split())) for _ in range(Q)]

follow_map = defaultdict(lambda : defaultdict(bool))


for t, a, b in q_list:
    if t == 1:
        follow_map[a][b] = True
    elif t == 2:
        follow_map[a][b] = False
    else:
        if follow_map[a][b] and follow_map[b][a]:
            print("Yes")
        else:
            print("No")
