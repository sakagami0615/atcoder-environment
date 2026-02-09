
from collections import defaultdict
from string import ascii_lowercase

def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(list(input()))

    cvt = {v: i for i, v in enumerate(ascii_lowercase)}

    row_counters = [[0] * len(ascii_lowercase) for _ in range(H)]
    col_counters = [[0] * len(ascii_lowercase) for _ in range(W)]

    row_kinds = [0] * H
    col_kinds = [0] * W

    n_row, n_col = H, W

    for i in range(H):
        for j in range(W):
            k = cvt[C[i][j]]
            row_counters[i][k] += 1
            if row_counters[i][k] == 1:
                row_kinds[i] += 1
    for j in range(W):
        for i in range(H):
            k = cvt[C[i][j]]
            col_counters[j][k] += 1
            if col_counters[j][k] == 1:
                col_kinds[j] += 1

    while True:
        row_remove, col_remove = [], []

        for i in range(H):
            if row_kinds[i] == 1 and n_col >= 2:
                row_remove.append(i)
        for j in range(W):
            if col_kinds[j] == 1 and n_row >= 2:
                col_remove.append(j)

        if (not row_remove) and (not col_remove):
            break

        for i in row_remove:
            for c in ascii_lowercase:
                row_counters[i][cvt[c]] = 0
            row_kinds[i] = 0
            for j in range(W):
                k = cvt[C[i][j]]
                col_counters[j][k] -= 1
                if col_counters[j][k] == 0:
                    col_kinds[j] -= 1
        for j in col_remove:
            for c in ascii_lowercase:
                col_counters[j][cvt[c]] = 0
            col_kinds[j] = 0
            for i in range(H):
                k = cvt[C[i][j]]
                row_counters[i][k] -= 1
                if row_counters[i][k] == 0:
                    row_kinds[i] -= 1

        n_row -= len(row_remove)
        n_col -= len(col_remove)

    print(n_row * n_col)


if __name__ == '__main__':
    main()
