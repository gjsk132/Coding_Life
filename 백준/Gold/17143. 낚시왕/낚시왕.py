from collections import deque

input = open(0).readline

R, C, M = map(int,input().split())

shark_cnt = M
dq = deque([])

table = [[0]*C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())

    table[r-1][c-1] = max(table[r-1][c-1], z)
    dq.append((r-1, c-1, s, d, z))

result = 0

for i in range(C):
    
    # fishing
    for j in range(R):
        if not table[j][i]:
            continue
        
        result += table[j][i]
        table[j][i] = 0
        break

    # shark_check
    for _ in range(shark_cnt):
        r, c, s, d, z = dq.popleft()

        if not table[r][c] == z:
            shark_cnt -= 1
            continue
        else:
            table[r][c] = 0
            dq.append(( r, c, s, d, z ))

    # shark_move
    for _ in range(shark_cnt):
        
        r, c, s, d, z = dq.popleft()

        # 1 : 위 / 2 : 아래 / 3 : 오른쪽 / 4 : 왼쪽
        if d <= 2:
            r += -s if d==1 else s

            while not 0 <= r < R:
                r = abs(r) if r < 0 else 2*R-2-r
                d = 1 if d==2 else 2

        else:
            c += s if d == 3 else -s

            while not 0 <= c < C:
                c = abs(c) if c <0 else 2*C-2-c
                d = 3 if d == 4 else 4

        table[r][c] = max(table[r][c], z)
        dq.append((r, c, s, d, z))
    
print(result)