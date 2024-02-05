from collections import deque

s, e = map(int,input().split())

limit = 100001

check = [False for _ in range(limit)]

dq = deque([(s, 0)])

while True:
    point, time = dq.popleft()
    
    if point == e:
        print(time)
        break
    
    for np in [ point + 1, point - 1, point*2 ]:
        if np < 0 or np >= limit or check[np]:
            continue
        
        check[np] = True
        dq.append((np, time+1))