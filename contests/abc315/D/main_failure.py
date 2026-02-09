
from collections import defaultdict

def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(list(input()))

    marked = [[False] * W for _ in range(H)]

    for i in range(H):
        appear = set()
        appear_pos = {}
        for j in range(W):
            c = C[i][j]
            if c in appear:
                marked[i][j] = True
                ai, aj = appear_pos[c]
                marked[ai][aj] = True
            appear.add(c)
            if c not in appear_pos:
                appear_pos[c] = (i, j)

    for j in range(W):
        appear = set()
        appear_pos = {}
        for i in range(H):
            c = C[i][j]
            if c in appear:
                marked[i][j] = True
                ai, aj = appear_pos[c]
                marked[ai][aj] = True
            appear.add(c)
            if c not in appear_pos:
                appear_pos[c] = (i, j)

    ans = 0
    for j in range(W):
        for i in range(H):
            if not marked[i][j]:
                ans += 1
            #else:
            #    C[i][j] = "."

    print(ans)

    #for line in C:
    #    print("".join(line))

if __name__ == '__main__':
    main()
