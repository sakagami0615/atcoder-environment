import sys
sys.setrecursionlimit(10 ** 6)

N, X, Y = map(int, input().split())

a_list = list(map(int, input().split()))

pt = [0, 0]


x_result = False
y_result = False

def x_dfs(i, x):
    global x_result
    if x_result: return
    i += 2
    if i >= N:
        if x == X:
            x_result = True
        return
    x_dfs(i, x + a_list[i])
    x_dfs(i, x - a_list[i])

def y_dfs(i, y):
    global y_result
    if y_result:
        return
    i += 2
    if i >= N:
        if y == Y:
            y_result = True
        return
    y_dfs(i, y + a_list[i])
    y_dfs(i, y - a_list[i])


x_dfs(0, a_list[0])
y_dfs(1, a_list[1])
y_dfs(1, -a_list[1])


if x_result and y_result:
    print("Yes")
else:
    print("No")