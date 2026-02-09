N, M = map(int, input().split())

x_sets = []
for _ in range(M):
    data = list(map(int, input().split()))
    x_sets.append(data[1:])

def solve():
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            is_ok = False
            for x_set in x_sets:
                if i not in x_set: continue
                if j in x_set:
                    is_ok = True
                    break
            if not is_ok:
                print("No")
                return
    print("Yes")

solve()