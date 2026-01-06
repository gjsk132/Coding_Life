import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

prefix = []
total = 0

for _ in range(N):
    total += int(input())
    prefix.append(total)

import bisect

for _ in range(Q):
    t = int(input())
    note = bisect.bisect_right(prefix, t)
    print(note + 1)
