from collections import deque


INF = float("INF")


def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    def appear_pos(mark):
        for i in range(H):
            for j in range(W):
                if A[i][j] == mark:
                    return i, j
        return None, None

    sy, sx = appear_pos("S")
    gy, gx = appear_pos("G")

    views = [[False] * W for _ in range(H)]

    for dx, dy, view_mark in [(1, 0, ">"), (-1, 0, "<"), (0, 1, "v"), (0, -1, "^")]:
        for i in range(H):
            for j in range(W):
                if A[i][j] == "#":
                    views[i][j] = True
                    continue
                elif A[i][j] != view_mark:
                    continue
                cx, cy = j + dx, i + dy
                views[i][j] = True
                while cx >= 0 and cy >= 0 and cx < W and cy < H:
                    if A[cy][cx] in [">", "<", "v", "^", "#"]:
                        break
                    views[cy][cx] = True
                    cx += dx
                    cy += dy

    visited = [[False] * W for _ in range(H)]

    que = deque()
    que.append((sx, sy, 0))
    visited[sy][sx] = True

    MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    ans = -1

    while que:
        cx, cy, dist = que.popleft()
        if cx == gx and cy == gy:
            ans = dist
            break

        for dx, dy in MOVE:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                continue
            if (not visited[ny][nx]) and (not views[ny][nx]):
                visited[ny][nx] = True
                que.append((nx, ny, dist + 1))

    print(ans)


if __name__ == '__main__':
    main()
