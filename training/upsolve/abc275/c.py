from collections import defaultdict

s_list = [input() for _ in range(9)]

mark_list = []
for r, line in enumerate(s_list):
    for c, token in enumerate(line):
        if token == "#":
            mark_list.append((r, c))

mark_dict = defaultdict(bool)
for mark in mark_list:
    mark_dict[mark] = True

n_marks = len(mark_list)

checked = set()

index = lambda r, c: r * 9 + c
rotate = lambda r, c, dr, dc: (r + dc, c - dr)

ans = 0
for i in range(n_marks - 1):
    for j in range(i + 1, n_marks):
        r0, c0 = mark_list[i]
        r1, c1 = mark_list[j]

        dr, dc = r1 - r0, c1 - c0
        r2, c2 = rotate(r1, c1, dr, dc)

        dr, dc = r2 - r1, c2 - c1
        r3, c3 = rotate(r2, c2, dr, dc)

        if mark_dict[(r2, c2)] and mark_dict[(r3, c3)]:
            idx0 = index(r0, c0)
            idx1 = index(r1, c1)
            idx2 = index(r2, c2)
            idx3 = index(r3, c3)
            idx_list = [idx0, idx1, idx2, idx3]
            idx_list.sort()
            idx_tuple = tuple(idx_list)

            if idx_tuple not in checked:
                checked.add(idx_tuple)
                ans += 1

print(ans)
