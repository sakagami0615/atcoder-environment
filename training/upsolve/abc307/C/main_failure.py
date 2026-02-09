#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')


class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans



def solve(H_A: int, W_A: int, A: "List[str]", H_B: int, W_B: int, B: "List[str]", H_X: int, W_X: int, X: "List[str]"):

    def get_pos(data):
        ret = SortedSet()
        for y, line in enumerate(data):
            for x, value in enumerate(line):
                if value == "#":
                    ret.add((x, y))
        return ret

    def get_rel_pos(pos):
        ret = SortedSet()
        base_p = None
        for i, p in enumerate(pos):
            if i == 0:
                base_p = p
                ret.add((0, 0))
            else:
                ret.add((p[0] - base_p[0], p[1] - base_p[1]))
        return ret

    def add_pos(pos, v):
        return SortedSet([(p[0] + v[0], p[1] + v[1]) for p in pos])

    def merge_pos(pos1, pos2):
        ret = SortedSet()
        for p in pos1: ret.add(p)
        for p in pos2: ret.add(p)
        return ret

    def is_equal(pos1, pos2):
        if len(pos1) != len(pos2): return False

        for p1, p2 in zip(pos1, pos2):
            if p1 != p2: return False
        return True

    pos_a = get_pos(A)
    pos_b = get_pos(B)
    pos_x = get_rel_pos(get_pos(X))

    max_h = max([H_A, H_B, H_X]) + 1
    max_w = max([W_A, W_B, W_X]) + 1

    def vis(pos):
        for h in range(max_h*2):
            for w in range(max_w*2):
                if (w, h) in pos:
                    print("# ", end="")
                else:
                    print(". ", end="")
            print()
        print("-----")

    for h_a in range(max_h):
        for w_a in range(max_w):

            for h_b in range(max_h):
                for w_b in range(max_w):

                    update_pos_a = add_pos(pos_a, (w_a, h_a))
                    update_pos_b = add_pos(pos_b, (w_b, h_b))
                    result_pos = merge_pos(update_pos_a, update_pos_b)
                    result_pos = get_rel_pos(result_pos)

                    if is_equal(result_pos, pos_x):
                        print(YES)
                        return

    print(NO)


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H_A = int(next(tokens))  # type: int
    W_A = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(H_A)]  # type: "List[str]"
    H_B = int(next(tokens))  # type: int
    W_B = int(next(tokens))  # type: int
    B = [next(tokens) for _ in range(H_B)]  # type: "List[str]"
    H_X = int(next(tokens))  # type: int
    W_X = int(next(tokens))  # type: int
    X = [next(tokens) for _ in range(H_X)]  # type: "List[str]"
    solve(H_A, W_A, A, H_B, W_B, B, H_X, W_X, X)

if __name__ == '__main__':
    main()
