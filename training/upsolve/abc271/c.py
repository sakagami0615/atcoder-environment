N = int(input())
a_list = list(map(int, input().split()))

append_set = set()
duple_cnt = 0

for a in a_list:
    if a not in append_set:
        append_set.add(a)
    else:
        duple_cnt += 1

sort_list = list(sorted(append_set))


ans = 0
for i in range(1, N + 1):
    if i in append_set:
        ans = i
    else:
        if duple_cnt > 1:
            duple_cnt -= 2
            ans = i
        elif duple_cnt == 1:
            duple_cnt -= 1
            if len(sort_list) < 1:
                break
            if i > sort_list[-1]:
                break
            pop_num = sort_list.pop()
            append_set.remove(pop_num)
            ans = i
        else:
            if len(sort_list) < 2:
                break
            if i > sort_list[-2]:
                break
            for _ in range(2):
                pop_num = sort_list.pop()
                append_set.remove(pop_num)
            ans = i

print(ans)
