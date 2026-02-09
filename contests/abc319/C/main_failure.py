from collections import defaultdict

def main():
    C = [list(map(int, input().split())) for _ in range(3)]

    numerator = 1
    denominator = 1


    for i in range(3):
        store = defaultdict(int)
        is_dup = False
        for j in range(3):
            c = C[i][j]
            if store[c] == 0:
                store[c] += 1
            else:
                is_dup = True
        if is_dup:
            numerator *= 2
            denominator *= 3

    for j in range(3):
        store = defaultdict(int)
        is_dup = False
        for i in range(3):
            c = C[i][j]
            if store[c] == 0:
                store[c] += 1
            else:
                is_dup = True
        if is_dup:
            numerator *= 2
            denominator *= 3

    store = defaultdict(int)
    is_dup = False
    for i in range(3):
        c = C[i][i]
        if store[c] == 0:
            store[c] += 1
        else:
            is_dup = True
    if is_dup:
        numerator *= 2
        denominator *= 3

    store = defaultdict(int)
    is_dup = False
    for i in range(3):
        c = C[3 - i - 1][i]
        if store[c] == 0:
            store[c] += 1
        else:
            is_dup = True
    if is_dup:
        numerator *= 2
        denominator *= 3

    print(numerator / denominator)


if __name__ == '__main__':
    main()
