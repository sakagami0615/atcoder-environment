from collections import deque


H, W = map(int, input().split())

C = ["#" + input() + "#" for _ in range(H)]
C = ["#" * (W + 2)] + C + ["#" * (W + 2)]

si, sj = None, None
for i in range(H + 2):
    for j in range(W + 2):
        if C[i][j] == "S":
            si, sj = i, j

MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]


visited = [[False] * (W + 2) for _ in range(H + 2)]

def bfs(si, sj):
    global visited

    if C[si][sj] != ".":
        return False

    que = deque()
    que.append((si, sj, 1))
    visited[si][sj] = True

    while que:
        i, j, d = que.popleft()

        for mi, mj in MOVE:
            ni, nj = i + mi, j + mj

            if C[ni][nj] == "S":
                if d > 1:
                    return True
                else:
                    continue

            if C[ni][nj] == "." and not visited[ni][nj]:
                que.append((ni, nj, d + 1))
                visited[ni][nj] = True

    return False


for mi, mj in MOVE:
    if bfs(si + mi, sj + mj):
        print("Yes")
        exit()

print("No")
