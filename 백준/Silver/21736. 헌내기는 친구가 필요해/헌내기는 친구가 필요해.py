input = open(0).readline

from collections import deque

h, w = map(int,input().split())

campus = []
offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]

dq = deque([])

answer = 0

for x in range(h):
    row = []
    for y, i in enumerate(input().rstrip()):
        if i == "O":
            row.append(0)
        elif i =="P":
            row.append(1)
        elif i =="X":
            row.append(2)
        else:
            row.append(3)
            dq.append((x, y))

    campus.append(row)

while dq:
    nx, ny = dq.popleft()

    for dx, dy in offset:
        px = nx + dx
        py = ny + dy

        if px < 0 or px >= h or py < 0 or py >= w:
            continue

        if campus[px][py] > 1:
            continue

        elif campus[px][py] == 1:
            answer += 1
        
        campus[px][py] = 2

        dq.append((px, py))

print(answer if not answer==0 else "TT")
