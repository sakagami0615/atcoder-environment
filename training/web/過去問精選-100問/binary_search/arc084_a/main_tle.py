import bisect

N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

A_list.sort()
B_list.sort()
C_list.sort()


ans = 0
for a in A_list:
    b_begin_idx = bisect.bisect_right(B_list, a)
    for b_idx in range(b_begin_idx, N):
        c_begin_idx = bisect.bisect_right(C_list, B_list[b_idx])
        ans += (N - c_begin_idx)

print(ans)
