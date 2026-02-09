N, K = map(int, input().split())

ai = list(range(1, N + 1))
ai += list(range(1, K))

def search_request(requests):
    msg = "? " + " ".join(requests)
    print(msg)

    return int(input())

ans_list = []

result_list = []
for i in range(N):
    requests = [ai[j] for j in range(i, i + K)]
    result = search_request(requests)
    result_list.append(result)




"""
   (1, 0, 1, 1, 0) (1, 0, 1

0 (1,2,3)  1, 0, 1
0 (2,3,4)     0, 1, 1
0 (3,4,5)        1, 1, 0
0 (4,5,1)           1, 0, 1
1 (5,1,2)              0, 1, 0
0 (1,2,3)                 1, 0, 1

<sample>
(1,2,3) + (2,3,4) = (1,4)
(4,5,1) + (1,4) = (5)

(1,2,3) + (2,3,4) + (4,5,1) = (5)
(2,3,4) + (3,4,5) + (5,1,2) = (1)
(3,4,5) + (4,5,1) + (1,2,3) = (2)
"""