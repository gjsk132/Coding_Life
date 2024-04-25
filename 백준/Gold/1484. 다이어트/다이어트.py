input = open(0).readline

gap = int(input())
max_weight = (gap)//2 + 1

low, high = 1, 2

ans = []

while high <= max_weight:
    tmp = high*high - low*low
    if tmp == gap:
        ans.append(high)
        high += 1
    elif tmp < gap:
        high += 1
    else:
        low += 1        
        
if ans:
    print(*ans)
else:
    print(-1)