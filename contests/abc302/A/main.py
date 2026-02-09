import math

A, B = map(int, input().split())

a = int(math.ceil(A / B))

diff = a * B - A

a -= diff // B

print(a)