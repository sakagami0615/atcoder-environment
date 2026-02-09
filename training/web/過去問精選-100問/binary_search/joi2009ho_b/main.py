import bisect


d = int(input())
n = int(input())
m = int(input())

d_list = [int(input()) for _ in range(n - 1)]
k_list = [int(input()) for _ in range(m)]

d_list.append(0)
d_list.append(d)

d_list.sort()

n_d_list = len(d_list)

ans = 0
for k in k_list:
    idx = bisect.bisect_left(d_list, k)
    if idx > 0:
        ans += min(abs(d_list[idx] - k), abs(d_list[idx - 1] - k))
    else:
        ans += abs(d_list[idx] - k)

print(ans)
