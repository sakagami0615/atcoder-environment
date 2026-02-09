from collections import deque


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

    def fill_view(sx, sy, dx, dy, view_mark):
        nonlocal views
        cx, cy = sx, sy
        is_view = False
        obs_mark = set([">", "<", "v", "^", "#"])
        obs_mark.remove(view_mark)
        while cx >= 0 and cy >= 0 and cx < W and cy < H:
            if A[cy][cx] == view_mark:
                is_view = True
            elif A[cy][cx] in obs_mark:
                is_view = False

            if is_view:
                views[cy][cx] = True
            elif A[cy][cx] == "#":
                views[cy][cx] = True
            cx += dx
            cy += dy

    for i in range(H):
        for x, y, dx, dy, view_mark in [(0, i, 1, 0, ">"), (W - 1, i, -1, 0, "<")]:
            fill_view(x, y, dx, dy, view_mark)
    for i in range(W):
        for x, y, dx, dy, view_mark in [(i, 0, 0, 1, "v"), (i, H - 1, 0, -1, "^")]:
            fill_view(x, y, dx, dy, view_mark)

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
