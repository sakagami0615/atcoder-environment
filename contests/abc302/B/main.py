H, W = map(int, input().split())

rc_list = [input() for _ in range(H)]

temp = "snuke"

def check(i, j):
    ans_list = []
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
                continue

            is_ok = True
            for n in range(len(temp)):
                ci = i + di * n
                cj = j + dj * n
                if ci < 0 or cj < 0 or ci > H - 1 or cj > W - 1:
                    is_ok = False
                    ans_list = []
                    break

                if rc_list[ci][cj] != temp[n]:
                    is_ok = False
                    ans_list = []
                    break

                ans_list.append((ci + 1, cj + 1))

            if is_ok:
                return True, ans_list

    return False, []

for i in range(H):
    for j in range(W):
        flg, ans_list = check(i, j)
        if flg:
            for ans in ans_list:
                print(*ans)
            exit()