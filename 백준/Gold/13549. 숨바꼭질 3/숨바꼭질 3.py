from collections import deque

start, end = map(int,input().split())

limit = 100002

check = [False for _ in range(limit)]

dq = deque([(start, 0)])

while dq:
    p, t = dq.popleft()
    
    check[p] = True
    
    if p == end:
        print(t)
        break
    
    for np in [p*2, p-1, p+1]:
        
        if np < 0 or np >= limit or check[np]:
            continue
        
        if np==p*2:
            dq.append((np,t))
        
        else:
            dq.append((np,t+1))