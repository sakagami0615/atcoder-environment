from collections import defaultdict


class UnionFind:

    def __init__(self, n, zero_index=False):
        self.n = n
        self.offset = 0 if zero_index else 1

        self.root = [-1] * (n + self.offset)

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            # Path compression
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.root[x] > self.root[y]:
            x, y = y, x

        self.root[x] += self.root[y]
        self.root[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, r in enumerate(self.root) if r < 0]

    def size(self, x):
        return -self.root[self.find(x)]

    def members(self, x):
        r = self.find(x)
        return [i + self.offset for i in range(self.n) if r == self.find(i + self.offset)]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group = defaultdict(list)

        for i in range(self.n):
            i += self.offset
            group[self.find(i)].append(i)

        return group

N = int(input())
ab_list = [list(map(int, input().split())) for _ in range(N)]


rank = 0
encoder = {}
decoder = {}
for a, b in ab_list:
    for x in [a, b]:
        if x not in encoder:
            encoder[x] = rank
            decoder[rank] = x
            rank += 1

uf = UnionFind(len(encoder))
for a, b in ab_list:
    encode_a, encode_b = encoder[a], encoder[b]
    uf.unite(encode_a, encode_b)

if 1 in encoder:
    print(max([decoder[x] for x in uf.members(encoder[1])]))
else:
    print(1)
