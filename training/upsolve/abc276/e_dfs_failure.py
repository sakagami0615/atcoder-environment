import sys
sys.setrecursionlimit(10 ** 6)


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


def dfs(m):

    visited = [[False] * W for _ in range(H)]
    n_pos = (s_pos[0] + m[0], s_pos[1] + m[1])
    visited[n_pos[0]][n_pos[1]] = True

    result = False

    def recursive(c_pos, dist=1):
        nonlocal result, visited

        if dist >= 4 and c_pos == s_pos:
            result = True
            return

        for m in MOVE:

            n_pos = (c_pos[0] + m[0], c_pos[1] + m[1])

            if n_pos[0] < 0 or n_pos[1] < 0 or n_pos[0] >= H or n_pos[1] >= H:
                continue
            if c_2d[n_pos[0]][n_pos[1]] == "#":
                continue
            if visited[n_pos[0]][n_pos[1]]:
                continue
            if n_pos == s_pos and dist < 4:
                continue
            visited[n_pos[0]][n_pos[1]] = True
            recursive(n_pos, dist + 1)
    recursive(n_pos)
    return result


for m in MOVE:
    if dfs(m):
        print("Yes")
        exit()

print("No")




