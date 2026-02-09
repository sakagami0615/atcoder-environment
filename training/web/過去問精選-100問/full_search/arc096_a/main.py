
A, B, C, X, Y = map(int, input().split())

value = 0
if C < (A + B) / 2:
    if X < Y:
        value += (X * 2) * C
        value += min((Y - X) * B, (Y - X) * C * 2)
    else:
        value += (Y * 2) * C
        value += min((X - Y) * A, (X - Y) * C * 2)
else:
    value += A * X
    value += B * Y

print(value)
