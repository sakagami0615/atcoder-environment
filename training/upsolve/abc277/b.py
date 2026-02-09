

cond1_set = set("HDCS")
cond2_set = set("A23456789TJQK")
cond3_set = set()

N = int(input())

S = [input() for _ in range(N)]

is_ok = True

for s in S:
    if s[0] not in cond1_set:
        is_ok = False
        break
    if s[1] not in cond2_set:
        is_ok = False
        break
    if s in cond3_set:
        is_ok = False
        break

    cond3_set.add(s)


if is_ok:
    print("Yes")
else:
    print("No")
