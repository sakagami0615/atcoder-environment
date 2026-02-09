
# TLE: pythonだと厳しそう。。。

H, W, N, h, w = map(int, input().split())


a_mat = {}
for i in range(1, N + 1):
    a_mat[i] = [[0] * W for _ in range(H)]

for _h in range(H):
    for _w, v in enumerate(map(int, input().split())):
        a_mat[v][_h][_w] = 1

# 積分画像作成
def create_integral_img(H, W, img):
    integ_img = [[0] * (W + 1) for _ in range(H + 1)]
    for hi in range(H):
        for wi in range(W):
            integ_img[hi + 1][wi + 1] = integ_img[hi][wi + 1] + integ_img[hi + 1][wi] - integ_img[hi][wi] + img[hi][wi]
    return integ_img


a_integ_mat = {}
for i in range(1, N + 1):
    a_integ_mat[i] = create_integral_img(H, W, a_mat[i])


for hi in range(H - h + 1):
    ans_list = []
    for wi in range(W - w + 1):
        cnt = 0
        for i in range(1, N + 1):
            total_num = a_integ_mat[i][-1][-1]

            tl_value = a_integ_mat[i][hi][wi]
            tr_value = a_integ_mat[i][hi][wi + w]
            bl_value = a_integ_mat[i][hi + h][wi]
            br_value = a_integ_mat[i][hi + h][wi + w]
            blank_num = br_value - tr_value - bl_value + tl_value

            if total_num - blank_num > 0:
                cnt += 1
        ans_list.append(cnt)

    print(*ans_list)