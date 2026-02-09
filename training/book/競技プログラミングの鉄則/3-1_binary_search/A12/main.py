#!/usr/bin/env python3
import bisect

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    def check(t):
        total = 0
        for a in A:
            total += t // a
        return total < K
    
    head = 0
    tail = 10 ** 10

    while head < tail - 1:
        mid = (tail + head) // 2
        if check(mid):
            head = mid
        else:
            tail = mid
    
    print(head + 1)
    

if __name__ == '__main__':
    main()
