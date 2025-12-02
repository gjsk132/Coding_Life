import heapq as hq

input = open(0).readline

N, M, H = map(int, input().split())

tomato = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

pos = []

for i in range(H):
    for j in range(M):
        for k in range(N):
            if tomato[i][j][k] == 1:
                hq.heappush(pos, (0, i, j, k))

offset = [(1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1),(0, -1, 0),(0, 1, 0)]

answer_day = 0

while pos:
    day, x, y, z = hq.heappop(pos)
    answer_day = max(answer_day, day)

    for dx, dy, dz in offset:
        nx, ny, nz = x + dx, y + dy, z + dz

        if nx < 0 or nx == H or ny < 0 or ny == M or nz < 0 or nz == N or not tomato[nx][ny][nz] == 0:
            continue
        
        tomato[nx][ny][nz] = 1
        hq.heappush(pos, (day+1, nx, ny, nz))

flag = False

for floor in tomato:
    if flag:
        break

    for row in floor:
        if 0 in row:
            flag = True
            break
    
print(answer_day if not flag else -1)