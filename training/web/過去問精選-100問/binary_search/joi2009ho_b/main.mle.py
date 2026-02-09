import bisect


d = int(input())
n = int(input())
m = int(input())

d_tuple_list = [(int(input()), i + 1) for i in range(n - 1)]
k_list = [int(input()) for _ in range(m)]

d_tuple_list.append((0, 0))
d_tuple_list.append((d, 0))

d_tuple_list.sort()

d_list = [val[0] for val in d_tuple_list]
n_d_list = len(d_list)


ans = 0
for k in k_list:
    idx = bisect.bisect_left(d_list, k)
    if idx > 0:
        ans += min(abs(d_list[idx] - k), abs(d_list[idx - 1] - k))
    else:
        ans += abs(d_list[idx] - k)

print(ans)
