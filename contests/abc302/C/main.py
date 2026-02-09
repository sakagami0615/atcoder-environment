import sys
import string
sys.setrecursionlimit(10 ** 8)

N, M = map(int, input().split())

cvt = {v: i for i, v in enumerate(string.ascii_lowercase)}


s_list = [[] for _ in range(N)]
for i in range(N):
    s = input()
    for j in range(M):
        s_list[i].append(cvt[s[j]])


edges = [set() for _ in range(N)]

for i in range(N - 1):
    for j in range(1, N):
        i_list = s_list[i]
        j_list = s_list[j]

        cnt = 0
        for iv, jv in zip(i_list, j_list):
            if iv != jv:
                cnt += 1

        if cnt == 1:
            edges[i].add(j)
            edges[j].add(i)


is_ok = False
visited = [False] * N

def dfs(v):
    global visited, is_ok
    cnt = 0
    for _v in visited:
        if _v: cnt += 1
    if cnt == N:
        is_ok = True
        return

    for n in edges[v]:
        if not visited[n]:
            visited[n] = True
            dfs(n)
            visited[n] = False



for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(i)
    if is_ok:
        print("Yes")
        exit()

print("No")
