input = open(0).readline

white = "W"
black = "B"

N, M = map(int, input().split())

board = list(input().strip() for _ in range(N))

fix_check = [[0 for _ in range(M)] for n in range(N)]

for n in range(N):
    for m in range(M):
        now_color = board[n][m]

        if (n + m)%2 == 0:
            if now_color == black:
                fix_check[n][m] = 1
        else:
            if now_color == white:
                fix_check[n][m] = 1

row_fix_cnt = [[] for _ in range(M-7)]

for n in range(N):
    for m in range(M-7):
        row_fix_cnt[m].append(sum(fix_check[n][m:m+8]))

answer = float('inf')

for m in range(M-7):
    for n in range(N-7):
        fix_total_cnt = sum(row_fix_cnt[m][n:n+8])
        answer = min(fix_total_cnt, 64-fix_total_cnt, answer)

print(answer)