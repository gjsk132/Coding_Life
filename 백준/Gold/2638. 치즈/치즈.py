from collections import deque
input = open(0).readline
n, m = map(int,input().split())

table = [[i for i in map(int,input().split())] for _ in range(n)]

melt = deque()
empty = deque([(0,0,0)])
table[0][0] = -1

result = 0

while empty or melt:
    if empty:
        px, py, day = empty.popleft()
    else:
        px, py, day = melt.popleft()
        result = max(day, result)
        
    for dx, dy in zip([-1,0,1,0],[0,1,0,-1]):
        nx = px+dx
        ny = py+dy
        
        if nx < 0 or ny < 0 or nx == n or ny == m or table[nx][ny] == -1:
            continue
        
        if table[nx][ny] == 0:
            table[nx][ny] = -1
            empty.append([nx, ny, day])
        
        elif table[nx][ny] == 2:
            table[nx][ny] = -1
            melt.append([nx, ny, day+1])
            
        else:
            table[nx][ny] += 1
print(result)