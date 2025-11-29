from collections import deque

input = open(0).readline

n, m = map(int, input().split())

move_map = [list(map(int, input().split())) for _ in range(n)]

distance_board = [[-1]*m for _ in range(n)]

dq = deque([])

offset = ((-1, 0), (0, 1), (1, 0), (0, -1))

def bfs(x, y):

    dq.append((x, y, 0))
    distance_board[x][y] = 0

    while dq:
        tx, ty, dist = dq.popleft()

        for dx, dy in offset:
            nx, ny = tx + dx, ty + dy

            if nx < 0 or nx == n or ny < 0 or ny == m or not move_map[nx][ny] == 1:
                continue
            
            if distance_board[nx][ny] == -1:
                dq.append((nx, ny, dist+1))
                distance_board[nx][ny] = dist+1
            
flag = False

for i in range(n):
    for j in range(m):
        if move_map[i][j] == 2:
            bfs(i, j)

        if move_map[i][j] == 0:
            distance_board[i][j] = 0

for row in distance_board:
    print(" ".join(map(str, row)))