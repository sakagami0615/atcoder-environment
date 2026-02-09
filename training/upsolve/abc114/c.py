import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())

ans = 0

def dfs(cur=""):
    global ans

    is_ok = True
    for num in ["3", "5", "7"]:
        if cur.count(num) == 0:
            is_ok = False
            break
    if is_ok:
        ans += 1

    for num in ["3", "5", "7"]:
        nxt = cur + num
        if int(nxt) <= N:
            dfs(nxt)

dfs()
print(ans)
