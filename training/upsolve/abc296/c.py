

N, X =map(int, input().split())

a_list = list(map(int, input().split()))

if X == 0:
    print("Yes")
    exit()

"""
A_i - A_j = X
A_i - X = A_j
"""

a_set = set(a_list)

for a_i in a_list:
    a_j = a_i - X
    if a_j in a_set:
        print("Yes")
        exit()

print("No")
