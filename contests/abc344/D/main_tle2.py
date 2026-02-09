#!/usr/bin/env python3
from string import ascii_lowercase

from heapq import heappop, heappush


class LowercaseEnglishHash:
    def __init__(self, is_blank=False):
        self.encoder_dict = {c: 10 + i for i, c in enumerate(ascii_lowercase)}
        self.decoder_dict = {10 + i: c for i, c in enumerate(ascii_lowercase)}
        if is_blank:
            self.encoder_dict[" "] = 99
            self.decoder_dict[99] = " "

    def encode(self, in_str):
        out_hash = 0
        unit = 1
        for c in in_str[::-1]:
            out_hash += self.encoder_dict[c] * unit
            unit *= 100
        return (out_hash, len(in_str))

    def decode(self, in_hash):
        out_str = ""
        hash_num = in_hash[0]
        while hash_num > 0:
            code = hash_num % 100
            hash_num //= 100
            out_str += self.decoder_dict[code]
        return out_str[::-1]

    def join(self, hash_a, hash_b):
        num = hash_a[0] * pow(10, hash_b[1] * 2) + hash_b[0]
        return (num, hash_a[1] + hash_b[1])

    def compare(self, hash_a, hash_b):
        if hash_a[0] < hash_b[0]:
            hash_a, hash_b = hash_b, hash_a

        diff_unit = pow(10, (hash_a[1] - hash_b[1]) * 2)
        num_a = hash_a[0] // diff_unit
        num_b = hash_b[0]
        return num_a == num_b


hash = LowercaseEnglishHash(is_blank=True)


def main():

    INF = float("INF")

    T = hash.encode(input())
    N = int(input())

    A, S = [], []
    for _ in range(N):
        line = input().split()
        A.append(int(line[0]))
        s_list = []
        for s in line[1:]:
            s_list.append(hash.encode(s))
        S.append(s_list)

    que = []
    # cost, value, index
    heappush(que, (0, None, 0))

    ans = -1
    while que:
        cur_c, cur_s, cur_i = heappop(que)

        if cur_s == T:
            ans = cur_c
            break

        if cur_i >= N:
            continue

        for s in S[cur_i]:
            nxt_s = s
            if cur_s:
                nxt_s = hash.join(cur_s, nxt_s)

            if hash.compare(T, nxt_s):
                heappush(que, (cur_c + 1, nxt_s, cur_i + 1))

            heappush(que, (cur_c, cur_s, cur_i + 1))

    print(ans)

if __name__ == '__main__':
    main()
