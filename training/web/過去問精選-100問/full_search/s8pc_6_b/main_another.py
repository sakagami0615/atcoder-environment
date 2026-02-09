
N = int(input())
A = [0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int, input().split())

A.sort()
B.sort()
s = A[N // 2]
g = B[N // 2]

print('//////')
print(s, g)
print('//////')

ans = 0
for a, b in zip(A, B):
    ans += abs(s - a)
    ans += abs(b - a)
    ans += abs(b - g)

print(ans)
