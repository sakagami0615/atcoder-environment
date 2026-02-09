import sys
sys.setrecursionlimit(10 ** 8)


def main():
    N = int(input())

    d_list = [list(map(int, input().split())) for _ in range(N - 1)]

    edges = [[] for _ in range(N)]
    connects = [[] for _ in range(N)]
    for i, line in enumerate(d_list):
        for j, d in enumerate(line):
            edges[i].append((j, d))
            edges[j].append((i, d))
            connects[i].append(j)
            connects[j].append(i)

    ans = 0
    visited = [False] * N
    used = []

    def dfs(curr, total_cost=0, is_connect=False):
        nonlocal ans, visited, used

        ans = max(ans, total_cost)
        visited[curr] = True
        if not is_connect:
            used.append(curr)
        for nxt, cost in edges[curr]:
            if not visited[nxt]:
                next_cost = cost
                if nxt in used:
                    flg = False
                    next_cost = 0
                    next_connect = False
                else:
                    flg = True
                    next_cost = next_cost
                    next_connect = True

                if flg:
                    used.append(nxt)
                dfs(nxt, total_cost + next_cost, next_connect)
                if flg:
                    used.pop()
        visited[curr] = False
        if not is_connect:
            used.pop()

    for start in range(N):
        dfs(start)

    print(ans)

if __name__ == '__main__':
    main()
