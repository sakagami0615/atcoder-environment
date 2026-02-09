X, K = map(int, input().split())


ans = X // (10 ** K) * (10 ** K)

src_num = X % (10 ** K)


for i in range(K):
    curr_num = src_num
    for j in range(i):
        curr_num //= 10
    mod = curr_num % 10
    if mod > 4:
        src_num += (10 ** (i + 1))
    src_num -= mod * (10 ** i)

ans += src_num
print(ans)
