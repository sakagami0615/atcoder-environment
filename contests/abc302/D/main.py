from bisect import bisect_left, bisect_right

# Segment Tree base class
class SegTree:
    def __init__(self, init_tree, op, e):
        self.op = op
        self.e = e
        self.n = 1 << (len(init_tree) - 1).bit_length()
        self.tree = [self.e()] * 2 * self.n
        for i, v in enumerate(init_tree):
            self.tree[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def get(self, k):
        return self.tree[self.n + k]

    def update(self, k, x):
        k += self.n
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = self.op(self.tree[2 * k], self.tree[2 * k + 1])

    def query(self, l, r):
        l += self.n
        r += self.n
        s = self.e()
        while l < r:
            if l & 1:
                s = self.op(s, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                s = self.op(s, self.tree[r])
            l >>= 1
            r >>= 1
        return s

# Range Maximum Query
class RMQ(SegTree):
    def op(x, y):
        return max(x, y)
    def e():
        return -float('INF')
    def __init__(self, init_tree):
        super().__init__(init_tree, RMQ.op, RMQ.e)

# Range minimum Query
class RmQ(SegTree):
    def op(x, y):
        return min(x, y)
    def e():
        return float('INF')
    def __init__(self, init_tree):
        super().__init__(init_tree, RmQ.op, RmQ.e)

# Range Sum Query
class RSQ(SegTree):
    def op(x, y):
        return x + y
    def e():
        return 0
    def __init__(self, init_tree):
        super().__init__(init_tree, RSQ.op, RSQ.e)


N, M, D = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort()

b_seg = RMQ(b_list)

ans = -1
for i, a in enumerate(a_list):

    a0 = a - D
    a1 = a + D

    i0 = bisect_left(b_list, a0)
    i1 = bisect_right(b_list, a1)

    ans = max(ans, a + b_seg.query(i0, i1))


print(ans)
