from itertools import permutations


def main():
    C = []
    for _ in range(3):
        C.extend(list(map(int, input().split())))


    LAT_IDX = [[0,1,2], [3,4,5], [6,7,8]]
    LON_IDX = [[0,3,6], [1,4,7], [2,5,8]]
    SLOPE_IDX = [[0,4,8], [2,4,6]]

    def check(curr):
        nonlocal visited
        for patterns in [LAT_IDX, LON_IDX, SLOPE_IDX]:
            for pattern in patterns:
                if curr not in pattern:
                    continue
                n_visit = 0
                visit_num = set()
                for idx in pattern:
                    if visited[idx]:
                        n_visit += 1
                        visit_num.add(C[idx])
                if n_visit == 2 and len(visit_num) == 1:
                    return False
        return True

    n_ok = 0
    n_pattern = 0
    for pattern in permutations([0,1,2,3,4,5,6,7,8]):
        visited = [False] * 9
        is_ok = True
        for idx in pattern:
            visited[idx] = True
            if not check(idx):
                is_ok = False
                break
        if is_ok:
            n_ok += 1
        n_pattern += 1

    print(n_ok / n_pattern)


if __name__ == '__main__':
    main()
