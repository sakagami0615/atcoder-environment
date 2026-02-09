#!/usr/bin/env python3
from collections import deque

def main():

    R, C = map(int, input().split())

    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    sy, sx = sy-1, sx-1
    gy, gx = gy-1, gx-1

    field = [list(input()) for _ in range(R)]
    field[sy][sx] = ''

    que = deque()

    que.append([sx, sy, 0])

    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while que:
        cx, cy, dist = que.popleft()

        if cx == gx and cy == gy:
            print(dist)
            break

        for m in move:
            nx = cx + m[0]
            ny = cy + m[1]

            if field[ny][nx] == '.':
                field[ny][nx] = ''
                que.append([nx, ny, dist + 1])


if __name__ == '__main__':
    main()
