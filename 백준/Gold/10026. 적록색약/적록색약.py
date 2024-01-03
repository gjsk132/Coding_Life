import sys
sys.setrecursionlimit(10**6)

input = open(0).readline
size = int(input())
area = [list(input().strip()) for i in range(size)]
blind = [['G' if j=='R' else j for j in i] for i in area]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x, y, color):
    for x_, y_ in zip(dx,dy):
        nx = x+x_
        ny = y+y_
        if nx < 0 or ny < 0 or nx == size or ny == size:
            continue
        if not area[nx][ny] == color:
            continue
        area[nx][ny] = 'X'
        bfs(nx,ny,color)
        
def findarea():
    cnt = 0
    for i in range(size):
        for j in range(size):
            if area[i][j] == 'X':
                continue
            cnt += 1
            bfs(i,j,area[i][j])
    print(cnt, end=" ")
    
findarea()
area = blind
findarea()