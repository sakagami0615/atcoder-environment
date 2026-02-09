import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

poly_a = np.poly1d(A[::-1])
poly_c = np.poly1d(C[::-1])

poly_b = poly_c / poly_a

b = [int(n) for n in poly_b[0].coef][::-1]
print(*b)
