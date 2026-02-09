from itertools import permutations


def main():
    C = [list(map(int, input().split())) for _ in range(3)]

    def check(r, c):
        # lat
        n_visit = 0
        visit_num = set()
        for j in range(3):
            cnum = C[r][j]
            if visited[r][j]:
                n_visit += 1
                visit_num.add(cnum)
        if n_visit == 2 and len(visit_num) == 1:
            return False

        # lon
        n_visit = 0
        visit_num = set()
        for i in range(3):
            cnum = C[i][c]
            if visited[i][c]:
                n_visit += 1
                visit_num.add(cnum)
        if n_visit == 2 and len(visit_num) == 1:
            return False

        # Slope1
        if r == c:
            n_visit = 0
            visit_num = set()
            for i in range(3):
                cnum = C[i][i]
                if visited[i][i]:
                    n_visit += 1
                    visit_num.add(cnum)
            if n_visit == 2 and len(visit_num) == 1:
                return False

        # Slope2
        if r - 2 == c or r == c - 2 or r - 2 == c - 2:
            n_visit = 0
            visit_num = set()
            for i in range(3):
                ri = 2 - i
                cnum = C[i][ri]
                if visited[i][ri]:
                    n_visit += 1
                    visit_num.add(cnum)
            if n_visit == 2 and len(visit_num) == 1:
                return False

        return True

    n_pos = 0
    n_cnt = 0
    for pattern in permutations([0,1,2,3,4,5,6,7,8]):
        visited = [[False] * 3 for _ in range(3)]
        is_ok = True
        for idx in pattern:
            r, c = idx // 3, idx % 3
            visited[r][c] = True

            if not check(r, c):
                is_ok = False
                break
        if is_ok:
            n_pos += 1
        n_cnt += 1

    print(n_pos / n_cnt)


if __name__ == '__main__':
    main()
