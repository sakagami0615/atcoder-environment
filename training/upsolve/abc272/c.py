N = int(input())

a_list = list(map(int, input().split()))

a_list.sort(reverse=True)

even_val = 0
odd_val = 0
even_cnt = 0
odd_cnt = 0
for a in a_list:
    if a % 2 == 0:
        if even_cnt < 2:
            even_val += a
            even_cnt += 1
    else:
        if odd_cnt < 2:
            odd_val += a
            odd_cnt += 1
    if odd_cnt == 2 and even_cnt == 2:
        break

if even_cnt < 2 and odd_cnt < 2:
    print(-1)
elif even_cnt == 2 and odd_cnt < 2:
    print(even_val)
elif odd_cnt == 2 and even_cnt < 2:
    print(odd_val)
else:
    print(max(odd_val, even_val))
