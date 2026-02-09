import sys
sys.setrecursionlimit(10 ** 6)


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for i in range(N):
        for j, num in enumerate(list(map(int, input().split()))):
            if j > 0:
                edges[i].append(num - 1)

    ans = []
    visited = [False] * N

    def dfs(cur):
        nonlocal ans
        for nxt in edges[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dfs(nxt)
        ans.append(cur + 1)

    dfs(0)
    print(*ans[:-1])


if __name__ == '__main__':
    main()
