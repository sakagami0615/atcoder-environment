from collections import defaultdict

S = input()

x = [0] * (len(S) + 1)

for i, s in enumerate(S):
    num = int(s)
    x[i + 1] = x[i] ^ (1 << num)

cnt_map = defaultdict(int)
for v in x:
    cnt_map[v] += 1

ans = 0
for cnt in cnt_map.values():
    ans += cnt * (cnt - 1) // 2

print(ans)
