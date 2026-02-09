
from collections import defaultdict

def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(list(input()))

    marked = [[False for _ in range(W)] for _ in range(H)]

    for i in range(H):
        counter = defaultdict(int)
        remove_set = set()
        for j in range(W):
            c = C[i][j]
            counter[c] += 1
            if counter[c] >= 2:
                remove_set.add(c)
        is_ok = True
        for n in counter[c].values():
            if n == 1:
                is_ok = False
                break
        if not is_ok: continue
        for j in range(W):
            c = C[i][j]
            if c in remove_set:
                marked[i][j] = True

    for j in range(W):
        counter = defaultdict(int)
        remove_set = set()
        for i in range(H):
            c = C[i][j]
            counter[c] += 1
            if counter[c] >= 2:
                remove_set.add(c)
        is_ok = True
        for n in counter[c].values():
            if n == 1:
                is_ok = False
                break
        if not is_ok: continue
        for i in range(H):
            c = C[i][j]
            if c in remove_set:
                marked[i][j] = True

    ans = 0
    for i in range(H):
        for j in range(W):
            if not marked[i][j]:
                ans += 1
            #else:
            #    C[i][j] = "."

    print(ans)

    #for line in C:
    #    print("".join(line))

if __name__ == '__main__':
    main()
