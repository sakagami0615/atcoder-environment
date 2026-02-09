import bisect


def LIS(N, A):
    INF = float("INF")
    dp = [INF] * N

    for a in A:
        i = bisect.bisect_left(dp, a)
        dp[i] = min(dp[i], a)

    lis = [a for a in dp if a != INF]
    return lis


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_D&lang=ja
if __name__ == "__main__":

    N = int(input())
    A = [int(input()) for _ in range(N)]

    lis = LIS(N, A)
    print(len(lis))
