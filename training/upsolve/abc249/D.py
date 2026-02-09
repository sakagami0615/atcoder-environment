
N = int(input())

MAX = 2 * (10 ** 5)

d_list = [0] * (MAX + 1)
for a in list(map(int, input().split())):
    d_list[a] += 1

ans = 0
for i in range(1, MAX + 1):
    j = 1
    while j * i <= MAX:
        k = i * j
        ans += d_list[i] * d_list[j] * d_list[k]
        j += 1

print(ans)

