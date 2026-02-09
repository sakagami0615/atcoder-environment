
N = int(input())

l = 1
r = N

#S = "0010011"

for _ in range(20):
    m = (l + r) // 2
    print(f"? {m}")
    ret_s = input()
    #ret_s = S[m - 1]

    if ret_s == "0":
        l = m
    else:
        r = m

print(l)