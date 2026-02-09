#!/usr/bin/env python3
from bisect import bisect_left


def main():
    N, Q = map(int, input().split())

    QUERY = [input().split() for _ in range(Q)]

    def encode_direct(c):
        if c == "U":
            return (0, 1)
        elif c == "D":
            return (0, -1)
        elif c == "R":
            return (1, 0)
        else:
            return (-1, 0)

    length = N
    pos = [[N - i, 0] for i in range(N)]
    for q, v in QUERY:
        if q == "1":
            curr_x, curr_y = pos[-1]
            curr_direct = encode_direct(v)
            curr_x += curr_direct[0]
            curr_y += curr_direct[1]
            pos.append([curr_x, curr_y])
            length += 1
        else:
            v = int(v) - 1
            print(*pos[length - v - 1])


if __name__ == '__main__':
    main()
