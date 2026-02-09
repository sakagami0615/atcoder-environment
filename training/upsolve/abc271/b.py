N, Q = map(int,input().split())

l_list = [list(map(int, input().split())) for _ in range(N)]

for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    print(l_list[s][t])