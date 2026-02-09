
"""
4 = (1, 3) (2, 2) (3, 1)

AB <= M (= N / 2)

A <= log(M)

"""

N = int(input())

data = [0] * (N + 1)

for n in range(1, N):

    for a in range(1, int(n ** 0.5) + 1):
        b = n // a
        if a * b == n:
            data[n] += 1
            if a != b:
                data[n] += 1


ans = 0
for ab in range(1, N):
    cd = N - ab
    ans += data[ab] * data[cd]

print(ans)
