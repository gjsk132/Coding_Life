input = open(0).readline

chess_board = [input().strip() for _ in range(8)]

answer = 0

for i in range(8):
    for j in range(8):
        if not (i + j)%2 and chess_board[i][j] == "F":
            answer += 1

print(answer)
