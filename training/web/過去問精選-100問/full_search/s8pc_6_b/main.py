
N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())


def counter(s, g):
    cnt = 0
    for a, b in zip(A, B):
        cnt += abs(s - a)
        cnt += abs(b - a)
        cnt += abs(b - g)
    return cnt


ans = float('Inf')
for i in range(N):
    for j in range(N):
        s = A[i]
        g = B[j]

        ans = min(ans, counter(s, g))

print(ans)
