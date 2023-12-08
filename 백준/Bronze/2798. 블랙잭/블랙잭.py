from itertools import combinations
import sys
n, tg = map(int, sys.stdin.readline().split())
nm = list(combinations(list(map(int,sys.stdin.readline().split())), 3))
re = 0
for i in nm:
    sm = sum(i)
    if sm == tg:
        re = sm
        break
    elif re < sm < tg:
        re = sm
print(re)    