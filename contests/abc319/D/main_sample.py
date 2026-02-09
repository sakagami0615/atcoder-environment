
def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    L = [l + 1 for l in L]

    def is_ok(win_size):
        n_row = 1
        curr = 0
        for l in L:
            if curr + l > win_size:
                n_row += 1
                curr = l
            else:
                curr += l

        if n_row <= M:
            return True
        else:
            return False

    top, bot = max(L) - 1, sum(L) + len(L)
    while top + 1 < bot:
        mid = (top + bot) // 2
        if is_ok(mid):
            bot = mid
        else:
            top = mid

    print(bot - 1)

if __name__ == '__main__':
    main()
