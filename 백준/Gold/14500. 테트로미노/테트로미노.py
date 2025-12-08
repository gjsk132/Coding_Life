input = open(0).readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

offset = [
    [(0, 1), (0, 2), (0, 3)], # I (가로)
    [(1, 0), (2, 0), (3, 0)], # I (세로)
    [(1, 0), (0, 1), (1, 1)], # O
    [(1, 0), (0, 1), (-1, 0)], # T (오른쪽)
    [(1, 0), (0, -1), (-1, 0)], # T (왼쪽)
    [(1, 0), (0, 1), (0, -1)], # T (아래쪽)
    [(-1, 0), (0, 1), (0, -1)], # T (위쪽)
    [(-1, 0), (-2, 0), (0, -1)], # L (위위왼)
    [(-1, 0), (-2, 0), (0, 1)], # L (위위오)
    [(1, 0), (2, 0), (0, -1)], # L (아아왼)
    [(1, 0), (2, 0), (0, 1)], # L (아아오)
    [(-1, 0), (0, -1), (0, -2)], # L (위오오)
    [(-1, 0), (0, 1), (0, 2)], # L (위왼왼)
    [(1, 0), (0, -1), (0, -2)], # L (아오오)
    [(1, 0), (0, 1), (0, 2)], # L (아왼왼)
    [(1, 0), (0, 1), (-1, 1)], # Z (아.오위)
    [(1, 0), (0, -1), (-1, -1)], # Z (아.왼위)
    [(0, -1), (-1, 0), (-1, 1)], # Z (왼.위오)
    [(0, -1), (1, 0), (1, 1)], # Z (왼.아오)    
]

answer = 0

def find_max_combo(x, y):
    max_c = 0
    
    base = board[x][y]

    for poses in offset:
        
        combo = base

        flag = True

        for dx, dy in poses:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx == N or ny < 0 or ny == M:
                flag = False
                break

            combo += board[nx][ny]
        
        if flag:
            max_c = max(max_c, combo)

    return max_c

for i in range(N):
    for j in range(M):
        answer = max(answer, find_max_combo(i, j))

print(answer)