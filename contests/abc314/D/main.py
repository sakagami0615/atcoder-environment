#!/usr/bin/env python3
def main():
    N = int(input())
    S = list(input())
    Q = int(input())


    T, X, C = [], [], []
    for _ in range(Q):
        tmp = input().split()
        T.append(int(tmp[0]))
        X.append(int(tmp[1]))
        C.append(tmp[2])

    t_end = None
    t_end_i = None
    for i in range(Q - 1, -1, -1):
        if T[i] != 1:
            t_end = T[i]
            t_end_i = i
            break

    flg = True
    for i, (t, x, c) in enumerate(zip(T, X, C)):
        if t == 1:
            S[x - 1] = c
        else:
            if flg and i >= t_end_i:
                s_tmp = "".join(S)
                if t_end == 2:
                    s_tmp = s_tmp.lower()
                elif t_end == 3:
                    s_tmp = s_tmp.upper()
                S = list(s_tmp)
                flg = False

    ans = ""
    for s in S:
        ans += s

    print(ans)


if __name__ == '__main__':
    main()
