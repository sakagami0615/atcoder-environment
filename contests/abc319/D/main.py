def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))

    def is_ok(win_size):
        n_row = 1
        curr = 0

        for l in L:
            curr += l + 1
            if curr > win_size + 1:
                n_row += 1
                curr = l + 1

        if n_row <= M:
            return True
        else:
            return False

    top, bot = max(L) - 1, sum(L) + N
    while top + 1 < bot:
        mid = (top + bot) // 2
        if is_ok(mid):
            bot = mid
        else:
            top = mid

    print(bot)

if __name__ == '__main__':
    main()
