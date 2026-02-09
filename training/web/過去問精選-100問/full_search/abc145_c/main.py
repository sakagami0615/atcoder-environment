import itertools

N = int(input())

XY = [list(map(float, input().split())) for _ in range(N)]

town_indexs = list(range(N))

comb_list = list(itertools.permutations(town_indexs))

ans = 0.0
for comb in comb_list:
    for i in range(1, N):
        prev = comb[i - 1]
        curr = comb[i]
        ans += ((XY[curr][0] - XY[prev][0]) ** 2 + (XY[curr][1] - XY[prev][1]) ** 2) ** 0.5

ans /= len(comb_list)

print(ans)
