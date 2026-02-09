from collections import defaultdict

N = int(input())
a_dict = defaultdict(int)
for i, a in enumerate(list(map(int, input().split()))):
    a_dict[i + 1] = a

Q = int(input())
q_list = [list(map(int, input().split())) for _ in range(Q)]

base = 0
for q in q_list:
    t = q[0]
    if t == 1:
        x = q[1]
        base = x
        a_dict = defaultdict(int)
    elif t == 2:
        i = q[1]
        x = q[2]
        a_dict[i] += x
    else:
        i = q[1]
        print(a_dict[i] + base)
