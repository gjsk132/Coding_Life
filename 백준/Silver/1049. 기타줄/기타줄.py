input = open(0).readline

n, m = map(int, input().split())

mins = 1000
minp = 1000

for i in range(m):
    s, p = map(int, input().split())
    if mins > s:
        mins = s
    if minp > p:
        minp = p

se = n//6
pa = n %6

result = 0

if mins <= minp*6:
    result += mins*se
else:
    result += minp*6*se

if mins <= minp*pa:
    result += mins
else:
    result += minp*pa

print(result)
