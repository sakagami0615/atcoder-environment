
N = int(input())
S = input()

cumsum = [[0] * 10 for _ in range(N + 1)]

for i, s in enumerate(S):
    num = int(s)
    for j in range(10):
        if j == num:
            cumsum[i + 1][num] = cumsum[i][num] + 1
        else:
            cumsum[i + 1][j] = cumsum[i][j]

ans_set = set()
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        tmp_set = set()
        for k in range(10):
            cnt = cumsum[-1][k] - cumsum[j + 1][k]
            if cnt > 0:
                tmp_set.add(k)

        i_str = S[i]
        j_str = S[j]
        for k in tmp_set:
            k_str = str(k)
            ans_set.add(i_str + j_str + k_str)

print(len(ans_set))
