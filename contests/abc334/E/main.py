#!/usr/bin/env python3

MOD = 998244353  # type: int


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


def mod_div(a, b, m):
    return a * pow(b, m - 2, m) % m


def main():
    H, W = map(int, input().split())
    F = [input() for _ in range(H)]


    pos2idx = defaultdict(lambda: None)
    red_pos = []
    cnt = 0
    for i in range(H):
        for j in range(W):
            if F[i][j] == "#":
                pos2idx[(i, j)] = cnt
                cnt += 1
            else:
                red_pos.append((i, j))
    n_red = len(red_pos)

    uf = UnionFind(len(pos2idx), True)
    for (i, j) in list(pos2idx.keys()):
        index = pos2idx[(i, j)]
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            target_index = pos2idx[(i + di, j + dj)]
            if target_index is not None:
                uf.unite(index, target_index)
    n_group = uf.group_size()

    ans = 0
    for i, j in red_pos:
        root_set = set()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            index = pos2idx[(i + di, j + dj)]
            if index is not None:
                root_set.add(uf.find(index))

        if len(root_set) == 0:
            ans += mod_div(n_group + 1, n_red, MOD)
            ans %= MOD
        else:
            ans += mod_div(n_group - len(root_set) + 1, n_red, MOD)
            ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
