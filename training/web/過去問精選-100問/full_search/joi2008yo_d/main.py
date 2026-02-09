M = int(input())

search_list = [list(map(int, input().split())) for _ in range(M)]

N = int(input())
star_list = [list(map(int, input().split())) for _ in range(N)]

diff_list = [[0, 0] for _ in range(M)]
for i in range(M - 1):
    diff_list[i][0] = search_list[i + 1][0] - search_list[i][0]
    diff_list[i][1] = search_list[i + 1][1] - search_list[i][1]

field_set = set()

for star in star_list:
    field_set.add((star[0], star[1]))


for i in range(N):
    star_x = star_list[i][0]
    star_y = star_list[i][1]
    pos_x = star_x
    pos_y = star_y
    for diff in diff_list:
        pos_x += diff[0]
        pos_y += diff[1]
        if (pos_x, pos_y) not in field_set:
            break
    else:
        search_x = search_list[0][0]
        search_y = search_list[0][1]
        print(star_x - search_x, star_y - search_y)
        exit()
