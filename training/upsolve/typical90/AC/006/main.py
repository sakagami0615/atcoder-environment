import string

INF = float('INF')

N, K = map(int, input().split())
S = input()


char_list = list(string.ascii_lowercase)
char_dict = {c: i for i, c in  enumerate(char_list)}

table = [[INF]*len(char_list) for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    for c in char_list:
        if c == S[i]:
            table[i][char_dict[c]] = i
        else:
            table[i][char_dict[c]] = table[i + 1][char_dict[c]]


ans = ''
pos = 0
for k in range(K):
    for i, c in enumerate(table[pos]):
        if N - c >= K - k:
            ans += char_list[i]
            pos = (c + 1)
            break

print(ans)
