N = int(input())
A = list(map(int, input().split()))

c_cumsum  = [0] * N
a_cumsum  = [0] * N
aa_cumsum = [0] * N

for i in range(N):
    if i == 0:
        c_cumsum[i] = 1
        a_cumsum[i] = A[i]
        aa_cumsum[i] = A[i] ** 2
    else:
        c_cumsum[i] = c_cumsum[i - 1] + 1
        a_cumsum[i] = a_cumsum[i - 1] + A[i]
        aa_cumsum[i] = aa_cumsum[i - 1] + A[i] ** 2

ans = 0
for i in range(1, N):
    term1 = (A[i] ** 2) * c_cumsum[i - 1]
    term2 = (2 * A[i]) * a_cumsum[i - 1]
    term3 = aa_cumsum[i - 1]
    ans += term1 - term2 + term3

print(ans)
