input = open(0).readline

size = int(input())
chart = [list(map(int, input().rstrip("\n"))) for i in range(size)]

area = []
cnt = 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def dfs(x, y):
    chart[y][x] = 2
    p_area = 1
    for j, i in zip(dy, dx):
        ny = y+j
        nx = x+i
        if nx < 0 or nx == size or ny < 0 or ny == size:
            continue
        if chart[ny][nx] == 2 or chart[ny][nx] == 0:
            continue
        p_area += dfs(nx,ny)

    return p_area

for my in range(size):
    for mx in range(size):
        if chart[my][mx] == 1:
            cnt += 1
            area.append(dfs(mx, my))

    
print(cnt)
print(*sorted(area), sep="\n")