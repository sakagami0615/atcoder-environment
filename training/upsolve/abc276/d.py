

import sys
import math

def gcd(a, b):
    return math.gcd(a, b)


N = int(input())
A_list = list(map(int, input().split()))

a_gcd = A_list[0]
for i in range(1, N):
    a_gcd = gcd(a_gcd, A_list[i])

ans = 0
for i in range(N):
    a_div = A_list[i] // a_gcd

    while a_div % 2 == 0:
        a_div //= 2
        ans += 1
    while a_div % 3 == 0:
        a_div //= 3
        ans += 1

    if a_div != 1:
        print(-1)
        sys.exit()


print(ans)
