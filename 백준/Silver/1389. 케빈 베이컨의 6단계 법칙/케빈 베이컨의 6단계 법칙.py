from collections import deque
input = open(0).readline
node, line = map(int,input().split())
array = [[0 for i in range(node+1)] for _ in range(node+1)]

for i in range(line):
    x, y = map(int,input().split())
    array[x][y] = 1
    array[y][x] = 1

for i in range(1,node+1):
    dq = deque([(i,0)])
    check = [False]*(node+1)
    check[i] = True
    
    while dq:
        nxt, dist = dq.popleft()
        for j in range(1, node+1):
            if (not check[j]) and (array[nxt][j]==1):
                array[i][j] = dist+1
                
                dq.append([j, dist+1])
                check[j] = True
    
low = 1e9
index = 0

for k, v in enumerate(array):
    if low > sum(v) > 0:
        low = sum(v)
        index = k

print(index)