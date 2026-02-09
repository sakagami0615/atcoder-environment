
s_list = [input() for _ in range(8)]

s_list.reverse()

ans = ""
for i, s in enumerate(s_list):
    if s.count("*") > 0:
        idx = s.index("*")
        ans = chr(idx + 97) + str(i + 1)

print(ans)