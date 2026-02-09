S = input()

S += '#'

ans = 0
acgt_set = set(['A', 'C', 'G', 'T'])

cnt = 0
for s in S:
    if s in acgt_set:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0

print(ans)
