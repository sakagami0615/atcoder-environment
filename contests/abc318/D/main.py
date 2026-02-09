import sys
sys.setrecursionlimit(10 ** 8)


def main():
    N = int(input())

    d_list = [list(map(int, input().split())) for _ in range(N - 1)]

    edges = [[] for _ in range(N)]
    for i, line in enumerate(d_list):
        for j, d in enumerate(line):
            edges[i].append((i + j + 1, d))
            edges[i + j + 1].append((i, d))

    ans = 0
    visited = [False] * N

    def dfs():
        nonlocal visited

        if all(visited):
            return 0

        cur = visited.index(False)
        visited[cur] = True
        num = 0
        for nxt, cost in edges[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                num = max(num, cost + dfs())
                visited[nxt] = False
        visited[cur] = False
        return num

    if N % 2 == 0:
        ans = dfs()
    else:
        for fix in range(N):
            visited[fix] = True
            ans = max(ans, dfs())
            visited[fix] = False

    print(ans)

if __name__ == '__main__':
    main()
