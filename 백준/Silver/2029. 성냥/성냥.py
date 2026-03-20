input = open(0).readline

board = [input().strip() for _ in range(10)]

count = 0

for b in board:
    count += b.count("-") + b.count("|")

count //= 2

square = 0

offset = ["+--+", "+--+--+", "+--+--+--+"]

for sx in [0, 3, 6]:
    for sy in [0, 3, 6]:
        
        flag = True
        if board[sx][sy:sy+len(offset[0])] == offset[0]:
            for idx in range(1, len(offset[0])-1):
                if not idx%3:
                    continue

                if not board[sx+idx][sy] == "|" or not board[sx+idx][sy+len(offset[0])-1] =="|":
                    flag = False
                    break

            if not board[sx+len(offset[0])-1][sy:sy+len(offset[0])] == offset[0]:
                flag = False
        else:
            flag = False
        
        if flag:
            square += int(flag)

for sx in [0, 3]:
    for sy in [0, 3]:
        
        flag = True
        if board[sx][sy:sy+len(offset[1])] == offset[1]:
            for idx in range(1, len(offset[1])-1):
                if not idx%3:
                    continue

                if not board[sx+idx][sy] == "|" or not board[sx+idx][sy+len(offset[1])-1] =="|":
                    flag = False
                    break

            if not board[sx+len(offset[1])-1][sy:sy+len(offset[1])] == offset[1]:
                flag = False
        else:
            flag = False
        
        if flag:
            square += int(flag)

sx, sy = 0, 0
flag = True
if board[sx][sy:sy+len(offset[2])] == offset[2]:
    for idx in range(1, len(offset[2])-1):
        if not idx%3:
            continue

        if not board[sx+idx][sy] == "|" or not board[sx+idx][sy+len(offset[2])-1] =="|":
            flag = False
            break

    if not board[sx+len(offset[2])-1][sy:sy+len(offset[2])] == offset[2]:
        flag = False
else:
    flag = False

if flag:
    square += int(flag)

print(24-count, square)