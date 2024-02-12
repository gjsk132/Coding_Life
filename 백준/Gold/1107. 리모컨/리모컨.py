input = open(0).readline

limit = 500001*2

cannel = []

target = int(input())

upDown = target - 100 if target > 100 else 100 - target

bottons = int(input())

cnt = 0

if bottons:
    broken = list(map(str,input().split()))

    for i in range(limit):
        cannel.append(False if any(b in str(i) for b in broken) else True)

    while cnt < upDown:
        
        if (cannel[target-cnt] if target>=cnt else False):
            cnt += len(str(target-cnt))
            break
        
        if (cannel[target+cnt] if target+cnt < limit else False):
            cnt += len(str(target+cnt))
            break
        
        cnt += 1
else:
    cnt += len(str(target))
            
print(min(cnt, upDown))