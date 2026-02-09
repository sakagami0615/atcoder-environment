
n = int(input())
p_list = list(map(int, input().split()))

for j in range(n - 2, -1, -1):
    if p_list[j] > p_list[j + 1]:
        break

for k in range(n - 1, -1, -1):
    if p_list[j] >p_list[k]:
        break

p_list[j], p_list[k] = p_list[k], p_list[j]

ans = p_list[:j + 1] + p_list[:j:-1]
print(*ans)
