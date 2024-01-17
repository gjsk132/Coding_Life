from collections import deque
input = open(0).readline
n, m = map(int,input().split())

paper = [list(map(int,input().split())) for _ in range(n)]
    
def bfs(x, y):
    dq = deque([(x,y)])
    paper[x][y] = 2
    
    area = 1
    
    while dq:
        px, py = dq.popleft()
        
        for dx, dy in [(-1, 0),(0, 1),(1, 0),(0, -1)]:
            nx = px+dx
            ny = py+dy
            
            if nx < 0 or nx == n or ny < 0 or ny == m:
                continue
            
            if paper[nx][ny] == 0 or paper[nx][ny] == 2:
                continue
            
            dq.append([nx,ny])
            paper[nx][ny] = 2
            area += 1
    
    return area

cnt = 0
high = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            cnt += 1
            high = max(high, bfs(i,j))
            
print(cnt)
print(high)