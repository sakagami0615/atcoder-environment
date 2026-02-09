n = int(input())

memo = {0: 1}
def f(i):
    if i in memo:
        return memo[i]

    a = f(i // 2)
    memo[i // 2] = a
    b = f(i // 3)
    memo[i // 3] = b

    return a + b

print(f(n))
