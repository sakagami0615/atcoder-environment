N = int(input())
S = input()

curr = S[0]
for s in S[1:]:
    if curr == s:
        print("No")
        exit()
    curr = s

print("Yes")