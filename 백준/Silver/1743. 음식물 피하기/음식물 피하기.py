from collections import deque

input = open(0).readline

height, width, trash = map(int,input().split())

passage = [[0 for _ in range(width+1)] for _ in range(height+1)]

for i in range(trash):
    x, y = map(int,input().split())
    passage[x][y] = 1

def bfs(x,y):
    queue = deque([(x,y)])
    area = 1
    
    while queue:
        px, py = queue.popleft()
        
        for i, j in zip([-1,0,1,0],[0,1,0,-1]):
            nx = px+i
            ny = py+j
            
            if 0 < nx <= height and 0 < ny <= width and passage[nx][ny] == 1:
                queue.append([nx,ny])
                passage[nx][ny] = 2
                area += 1
    return area

result = []

for i in range(1, height+1):
    for j in range(1, width+1):
        if passage[i][j] == 1:
            passage[i][j] = 2
            result.append(bfs(i,j))

print(max(result))