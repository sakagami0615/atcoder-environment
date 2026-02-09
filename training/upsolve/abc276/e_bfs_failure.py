from collections import deque


H, W = map(int, input().split())

c_2d = [input() for _ in range(H)]

visited = [[False] * W for _ in range(W)]

s_pos = None
for i in range(H):
    for j in range(W):
        if c_2d[i][j] == "S":
            s_pos = (i, j)

stack = []
stack.append((s_pos, None))

MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]

visited = [[False] * W for _ in range(H)]


def bfs(m):

    visited = [[False] * W for _ in range(H)]
    c_pos = (s_pos[0], s_pos[1])

    for _ in range(2):
        c_pos = (c_pos[0] + m[0], c_pos[1] + m[1])
        if c_pos[0] < 0 or c_pos[1] < 0 or c_pos[0] >= H or c_pos[1] >= H:
            return False
        if c_2d[c_pos[0]][c_pos[1]] != ".":
            return False

        visited[c_pos[0]][c_pos[1]] = True

    que = deque()
    que.append((c_pos, 2))

    while que:
        c_pos, dist = que.popleft()
        if c_pos == s_pos and dist >= 4:
            return True

        for m in MOVE:
            n_pos = (c_pos[0] + m[0], c_pos[1] + m[1])
            if n_pos[0] < 0 or n_pos[1] < 0 or n_pos[0] >= H or n_pos[1] >= W:
                continue
            if c_2d[n_pos[0]][n_pos[1]] == "#" or visited[n_pos[0]][n_pos[1]]:
                continue

            que.append((n_pos, dist + 1))
            visited[n_pos[0]][n_pos[1]] = True

    return False


for m in MOVE:
    if bfs(m):
        print("Yes")
        exit()

print("No")
