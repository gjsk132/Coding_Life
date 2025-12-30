input = open(0).readline

a, b = input().strip(), input().strip()
board = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i, ai in enumerate(a):
    for j, bj in enumerate(b):
        board[i+1][j+1] = max(board[i][j]+(1 if ai==bj else 0), board[i+1][j], board[i][j+1])

print(board[len(a)][len(b)])