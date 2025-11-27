input = open(0).readline

# 세로, 가로, 높이
y, x, z = map(int, input().split())

# board[z][y][x]
board = [[input().strip() for _ in range(y)] for _ in range(z)]

mine = [[[0 for _ in range(x)] for _ in range(y)] for _ in range(z)]

def add_mine(dz, dy, dx):
    for px in (dx-1, dx, dx+1):

        if px < 0 or px == x:
            continue

        for py in (dy-1, dy, dy+1):

            if py < 0 or py == y:
                continue

            for pz in (dz-1, dz, dz+1):

                if pz < 0 or pz == z:
                    continue

                mine[pz][py][px] += 1

for i in range(z):
    for j in range(y):
        for k in range(x):
            if not board[i][j][k] == "*":
                continue
            
            add_mine(i, j, k)

for i in range(z):
    for j in range(y):
        for k in range(x):
            if board[i][j][k] == "*":
                print("*", end="")
            else:
                print(mine[i][j][k]%10, end="")
        print()