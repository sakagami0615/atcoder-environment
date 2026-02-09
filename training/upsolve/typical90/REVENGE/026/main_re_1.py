from collections import deque

N = int(input())

edges = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

node_colors = [0] * N
visited = [False] * N

que = deque()
que.append((0, 0))
visited[0] = True

cnt_0 = 0
cnt_1 = 0
while que:
    i, c = que.popleft()
    node_colors[i] = c
    if c == 0:
        cnt_0 += 1
    else:
        cnt_1 += 1

    for n in edges[i]:
        if visited[n]:
            continue
        que.append((n, 1 - c))
        visited[n] = True

max_color = 0 if cnt_0 >= cnt_1 else 1
cnt = 0
ans_list = []

for i, c in enumerate(node_colors):
    if c == max_color:
        ans_list.append(i + 1)
        cnt += 1
        if cnt >= N // 2:
            break

print(*ans_list)