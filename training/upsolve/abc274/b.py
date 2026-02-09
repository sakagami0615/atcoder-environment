
h, w = map(int, input().split())

ans_list = [0] * w

for _ in range(h):
    for i, c in enumerate(input()):
        if c == "#":
            ans_list[i] += 1
print(*ans_list)
