from math import ceil

N = int(input())

m = 0
while 2 ** m < N:
    m += 1

drink = [[] for _ in range(m)]

for i in range(m):
    for j in range(N):
        if j & (1 << i):
            drink[i].append(j + 1)

print(m)
for v in drink:
    print(len(v), *v)

result = input()
ans = 0
for i, c in enumerate(result):
    if c == "1":
        ans |= (1 << i)

print(ans + 1)
