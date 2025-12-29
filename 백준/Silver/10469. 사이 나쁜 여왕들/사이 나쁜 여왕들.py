input = open(0).readline

check = [[False]*15 for _ in range(4)]

board = [input().strip() for _ in range(8)]

flag = False

cnt = 0

for r in range(8):

    if flag:
        break

    for c in range(8):
        if not (e:=board[r][c]) == "*":
            continue

        cnt += 1

        if check[0][r]:
            flag = True
            break
        else:
            check[0][r] = True

        if check[1][c]:
            flag = True
            break
        else:
            check[1][c] = True
        
        if check[2][r-c]:
            flag = True
            break
        else:
            check[2][r-c] = True

        if check[3][r+c]:
            flag = True
            break
        else:
            check[3][r+c] = True


print("valid" if not flag and cnt == 8 else "invalid")