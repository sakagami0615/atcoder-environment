import sys

N, M = map(int, input().split())
a_list = list(map(int, input().split()))

if N == 1:
    print(0)
    sys.exit()

a_list.sort()
a_sum = sum(a_list)

ans = float("INF")

begin_idx = 0
prev = a_list[0]
store = prev
for i in range(1, N*2):
    # 条件を満たしたまま一周した場合
    mod_i = i % N
    if begin_idx == 0 and mod_i == 0:
        ans = 0
        break

    curr = a_list[mod_i]

    # 条件を満たさなくなったタイミングで最小値と比較
    if not (curr == prev or curr == (prev + 1) % M):
        ans = min(ans, a_sum - store)
        if i >= N:
            break
        begin_idx = mod_i
        store = curr
    # 条件を満たすときは、和を求めておく
    else:
        store += curr

    prev = curr

print(ans)
