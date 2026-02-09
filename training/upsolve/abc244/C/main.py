
N = int(input())

store_set = set([i + 1 for i in range(2 * N + 1)])

for _ in range(2 * N + 1):

    own = store_set.pop()
    print(own)

    enemy = int(input())
    if enemy == 0:
        break
    store_set.remove(enemy)
