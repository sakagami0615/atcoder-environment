
N = int(input())
A, B, C = map(int, input().split())

n_a = N // A
n_b = N // B

max_l = 9999
ans = 9999
for a in range(max_l):
    a_num = A * a
    if a_num > N:
        break

    for b in range(max_l - a):
        b_num = B * b
        if a_num + b_num > N:
            break

        c_num = N - a_num - b_num

        if c_num % C == 0:
            c = c_num // C
            ans = min(ans, (a + b + c))


print(ans)