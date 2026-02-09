from collections import deque

N, M = map(int, input().split())


move = []
for i in range(-N, N + 1):
    for j in range(-N, N + 1):
        if i ** 2 + j ** 2 == M:
            move.append((i, j))


ans_list = [[-1] * N for _ in range(N)]

que = deque()
que.append((0, 0))
ans_list[0][0] = 0

while que:
    i, j = que.popleft()

    for m in move:
        k, l = i + m[0], j + m[1]
        if 0 <= k < N and 0 <= l < N:
            if ans_list[k][l] == -1:
                ans_list[k][l] = ans_list[i][j] + 1
                que.append((k, l))


for ans in ans_list:
    print(*ans)
