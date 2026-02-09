
def Divisor(N):
    root_n = int(N ** 0.5)
    div_list = []
    for d in range(1, root_n + 1):
        if N % d == 0:
            div_list.append(d)
            div_list.append(N // d)

    div_list.sort()
    return div_list

N = int(input())

ans = 0
for n in range(1, N + 1, 2):
    div_list = Divisor(n)
    if len(div_list) == 8:
        ans += 1

print(ans)
