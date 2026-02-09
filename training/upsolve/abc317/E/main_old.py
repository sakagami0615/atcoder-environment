from collections import deque
from bisect import bisect_left, bisect_right


def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    def appear_pos(mark):
        for i in range(H):
            for j in range(W):
                if A[i][j] == mark:
                    return i, j
        return None, None

    def lat_appear_list(mark):
        allow_list = [[] for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if A[i][j] == mark:
                    allow_list[i].append(j)
        return allow_list

    def lon_appear_list(mark):
        allow_list = [[] for _ in range(W)]
        for j in range(W):
            for i in range(H):
                if A[i][j] == mark:
                    allow_list[j].append(i)
        return allow_list

    sy, sx = appear_pos("S")
    gy, gx = appear_pos("G")

    lon_r_allow = lon_appear_list(">")
    lon_l_allow = lon_appear_list("<")
    lon_obstacle = lon_appear_list("#")

    lat_r_allow = lat_appear_list("v")
    lat_l_allow = lat_appear_list("^")
    lat_obstacle = lat_appear_list("#")

    visited = [[False] * W for _ in range(H)]

    que = deque()
    que.append((sx, sy, 0))
    visited[sy][sx] = True

    MOVE = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_ok(nx, ny):

        if A[ny][nx] != ".":
            return False

        def is_into_view(r_allow, l_allow, obstacle, n):
            r0_a_idx = bisect_left(r_allow, n) - 1
            r1_a_idx = bisect_left(r_allow, n)
            l0_a_idx = bisect_left(l_allow, n) - 1
            l1_a_idx = bisect_left(l_allow, n)
            l_o_idx = bisect_left(obstacle, n) - 1
            r_o_idx = bisect_left(obstacle, n)

            is_r0_a = r0_a_idx > -1
            is_r1_a = r1_a_idx < len(r_allow) - 1
            is_l0_a = l0_a_idx > -1
            is_l1_a = l1_a_idx < len(l_allow) - 1
            is_l_o = l_o_idx > -1
            is_r_o = r_o_idx < len(obstacle) - 1

            # TODO; 二分探索による判定処理を書けば良い
            """
            if is_r0_a:

                if (is_l1_a and (r0_a_idx < n < l1_a_idx)) or (is_l_o and (r0_a_idx < n < l_o_idx)):
                    return False
            elif is_l1_a:
                if is_r0_a and (l1_a_idx > n > r0_a_idx):
                    return False
                elif is_r_o and (l1_a_idx > n > r_o_idx):
                    return False
            """
            return True

        if is_into_view(lat_r_allow[ny], lat_l_allow[ny], lat_obstacle[ny], nx):
            return False
        if is_into_view(lon_r_allow[nx], lon_l_allow[nx], lon_obstacle[nx], ny):
            return False
        return True


    ans = -1

    while que:
        cx, cy, dist = que.popleft()
        print((cx, cy, dist))
        if cx == gx and cy == gy:
            ans = dist
            break


        for dx, dy in MOVE:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= W or ny >= H:
                continue
            if not visited[ny][nx] and is_ok(nx, ny):
                visited[ny][nx] = True
                que.append((nx, ny, dist + 1))

    print(ans)


if __name__ == '__main__':
    main()
