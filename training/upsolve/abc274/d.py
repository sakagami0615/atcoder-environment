
N, X, Y = map(int, input().split())

a_list = list(map(int, input().split()))

x_set = set()
y_set = set()

x_set.add(a_list[0])
y_set.add(0)

for i in range(1, N):
    curr_set = set()
    if i % 2 == 0:
        for x in x_set:
            curr_set.add(x + a_list[i])
            curr_set.add(x - a_list[i])
        x_set = curr_set
    else:
        for y in y_set:
            curr_set.add(y + a_list[i])
            curr_set.add(y - a_list[i])
        y_set = curr_set

if X in x_set and Y in y_set:
    print("Yes")
else:
    print("No")