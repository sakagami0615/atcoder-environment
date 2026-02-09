from collections import defaultdict

N, K = map(int, input().split())

s_list = [input() for _ in range(N)]


ans = 0
for p in range(2 ** N):
    store = defaultdict(int)
    for b in range(N):
        if (p >> b) & 1:
            for s in s_list[b]:
                store[s] += 1
    curr = 0
    for v in store.values():
        if v == K:
            curr += 1
    ans = max(ans, curr)

print(ans)
