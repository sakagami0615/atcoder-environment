N = int(input())

"""
X = 1 + (1 - p)X
(1 - (1 - p))X = 1
X = 1 / p

p = 1 / ((N - i) / N)
p = N / (N - i)
"""

ans = 0
for i in range(1, N):
    ans += N / (N - i)

print(f"{ans:.10f}")
