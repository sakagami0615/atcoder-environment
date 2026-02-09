#!/usr/bin/env python3
import bisect

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    
    ind = bisect.bisect_left(A, X)
    print(ind + 1)

if __name__ == '__main__':
    main()
