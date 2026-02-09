from collections import defaultdict

N, Q = map(int, input().split())

q_list = [list(map(int, input().split())) for _ in range(Q)]

status = defaultdict(int)

for q, x in q_list:
    if q == 1:
        status[x] += 1
    elif q == 2:
        status[x] += 2
    else:
        if status[x] >= 2:
            print("Yes")
        else:
            print("No")
