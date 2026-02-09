n = int(input())

ans_list = [0] * (2*n + 1)

cnt = 0
for a in map(int, input().split()):
    ans_list[2*cnt + 1] = ans_list[a - 1] + 1
    ans_list[2*cnt + 2] = ans_list[a - 1] + 1
    cnt += 1

for ans in ans_list:
    print(ans)
