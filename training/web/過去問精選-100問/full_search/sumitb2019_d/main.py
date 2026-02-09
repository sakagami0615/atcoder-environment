
N = int(input())
S = input()


def ok(i, j, k):

    check_idx = 0
    store = [i, j, k]

    for i in range(N):
        if store[check_idx] == S[i]:
            check_idx += 1
            if check_idx >= 3:
                return True

    return False


ans = 0
for i in range(10):
    for j in range(10):
        for k in range(10):
            ans += int(ok(str(i), str(j), str(k)))

print(ans)

