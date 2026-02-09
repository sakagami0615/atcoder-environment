#!/usr/bin/env python3
from string import ascii_lowercase


def main():
    encoder = {c: 10 + i for i, c in enumerate(ascii_lowercase)}
    encoder[""] = 0

    UNITS = [1]
    for _ in range(10000):
        UNITS.append(UNITS[-1] * 10)

    def str_to_num(in_str):
        num = 0
        n = len(in_str)
        unit = pow(10, (n - 1) * 2)
        for c in in_str:
            num += encoder[c] * unit
            unit //= 100
        return num

    def compare(t, n_t, s, n_s):
        if s == 0:
            return True, t, n_t

        n_diff = n_t - n_s
        if n_diff < 0:
            return False, "", INF

        unit = UNITS[n_diff]
        pt = t // unit
        if pt != s:
            return False, "", INF

        dt = t - pt * unit
        return True, dt, n_diff

    INF = float("INF")

    T = input()
    NT = len(T) * 2
    T = str_to_num(T)
    N = int(input())

    A, S, NS = [], [], []
    memo = []
    for _ in range(N):
        line = input().split()
        A.append(int(line[0]))
        s_list = []
        ns_list = []
        memo_list = []
        for s in line[1:] + [""]:
            ns_list.append(0 if s == "" else len(s) * 2)
            s_list.append(str_to_num(s))
            memo_list.append(INF)
        S.append(s_list)
        NS.append(ns_list)
        memo.append(memo_list)

    ans = INF


    def dfs(idx=0, t=T, n_t=NT, cur=0, n_cur=0, cost=0):
        nonlocal ans

        if T == cur:
            ans = min(ans, cost)
            return ans
        if idx == N:
            return INF

        for s_i, (s, n_s) in enumerate(zip(S[idx], NS[idx])):
            if s == 0:
                if memo[idx][s_i] <= cost:
                    continue
            else:
                if memo[idx][s_i] <= cost + 1:
                    continue

            result, nxt_t, nxt_nt = compare(t, n_t, s, n_s)
            if result:
                if s == 0:
                    result_cost = dfs(idx + 1, nxt_t, nxt_nt, cur, n_cur, cost)
                    memo[idx][s_i] = min(memo[idx][s_i], result_cost)
                else:
                    if cur == 0:
                        nxt = s
                    else:
                        nxt = cur * UNITS[n_s] + s
                    result_cost = dfs(idx + 1, nxt_t, nxt_nt, nxt, n_cur + n_s, cost + 1)
                    memo[idx][s_i] = min(memo[idx][s_i], result_cost)
        return INF

    dfs()
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
