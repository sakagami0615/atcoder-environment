import bisect

N = int(input())

A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
C_list = list(map(int, input().split()))

A_list.sort()
B_list.sort()
C_list.sort()


ans = 0
for b in B_list:
    a_tail_idx = bisect.bisect_left(A_list, b)
    c_head_idx = bisect.bisect_right(C_list, b)
    ans += a_tail_idx * (N - c_head_idx)

print(ans)
