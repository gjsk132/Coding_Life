from collections import deque
input = open(0).readline
size = int(input())

dist = [[0 for i in range(size+1)] for _ in range(size+1)]

for i in range(size-1):
    a, b, c = map(int,input().split())
    dist[a][b] = dist[b][a] = c

dq = deque([(1,0)])

check = [False]*(size+1)

result = 0

while dq:
    now, cost = dq.popleft()
    
    if not check[now]:
        check[now] = True
        for k, v in enumerate(dist[now]):
            if (not v == 0) and (not check[k]):
                dq.append([k, cost+v])
                result = max(result, cost+v)

print(result)