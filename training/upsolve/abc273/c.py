from bisect import bisect_left, bisect_right

N = int(input())

a_list = list(map(int, input().split()))
a_list.sort()
a_unique = list(set(a_list))
a_unique.sort()

n_a_unique = len(a_unique)

for k in range(N):

    if n_a_unique <= k:
        print(0)
        continue

    tgt_a = a_unique[n_a_unique - k - 1]
    l_idx = bisect_left(a_list, tgt_a)
    r_idx = bisect_right(a_list, tgt_a)

    print(r_idx - l_idx)
