from itertools import combinations
n, tg = map(int, input().split())
nm = list(combinations(list(map(int,input().split())), 3))
re = 0
for i in nm:
    sm = sum(i)
    if sm == tg:
        re = sm
        break

    elif re < sm < tg:
        re = sm
print(re)    