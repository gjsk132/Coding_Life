input = open(0).readline

rocks_cnt = int(input())
rocks = list(map(int, input().split()))

left, right = rocks[0], rocks[1]

for r in rocks[2:]:
    if left > right:
        right += r
    else:
        left += r

offset = [100, 50, 20, 10, 5, 2, 1]

gap = max(left,right) - min(left,right)

cnt = 0

for o in offset:
    if not gap:
        break
    
    cnt += gap//o
    gap %= o

print(cnt)