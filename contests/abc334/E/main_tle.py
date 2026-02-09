#!/usr/bin/env python3

MOD = 998244353  # type: int


from collections import defaultdict
from copy import deepcopy


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

    uf = UnionFind(H * W)

    pos2idx = lambda i, j: i * W + j

    red_pos_list = []
    for i in range(H):
        for j in range(W):
            if F[i][j] == "#":
                for di, dj in [(0, 1), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if ni >= H or nj >= W: continue
                    if F[ni][nj] == "#":
                        uf.unite(pos2idx(i, j), pos2idx(ni, nj))
            else:
                red_pos_list.append((i, j))

    root_set = set()
    for i in range(H):
        for j in range(W):
            if F[i][j] == "#":
                root_set.add(uf.find(pos2idx(i, j)))
    n_connect = len(root_set)
    n_pos = len(red_pos_list)

    ans = 0
    for i, j in red_pos_list:
        use_uf = deepcopy(uf)
        prev_root_set, update_root_set = set(), set()

        search_pos_list = []
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= H or nj >= W: continue
            if F[ni][nj] == "#":
                search_pos_list.append((ni, nj))

        if len(search_pos_list) > 0:
            for ni, nj in search_pos_list:
                use_uf.unite(pos2idx(i, j), pos2idx(ni, nj))
            for ni, nj in search_pos_list:
                prev_root_set.add(uf.find(pos2idx(ni, nj)))
                update_root_set.add(use_uf.find(pos2idx(ni, nj)))
            n_dels = len(prev_root_set) - len(update_root_set)
            ans += mod_div(n_connect - n_dels, n_pos, MOD)
        else:
            ans += mod_div(n_connect + 1, n_pos, MOD)
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
