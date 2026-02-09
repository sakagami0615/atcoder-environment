
N = int(input())


def request(a, b, c, d):
    print(f"? {a} {b} {c} {d}")
    t = int(input())
    if t == -1:
        exit()
    return t

def submit(x, y):
    print(f"! {x} {y}")


a, b = 1, N + 1
c, d = 1, N + 1

while a + 1 < b:
    m = (a + b) // 2
    t = request(a, m - 1, 1, N)
    if m - a == t:
        a = m
    else:
        b = m

while c + 1 < d:
    m = (c + d) // 2
    t = request(1, N, c, m - 1)
    if m - c == t:
        c = m
    else:
        d = m

submit(a, c)
