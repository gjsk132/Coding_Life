def solution(game_board, table):
    
    puzzles, emptys = [], []

    offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    tx, ty = len(table), len(table[0])
    gx, gy = len(game_board), len(game_board[0])

    def dfs_table(x, y):
        
        puzzle = [(x, y)]

        for dx, dy in offset:
            nx, ny = x + dx, y + dy
            
            if not 0 <= nx < tx or not 0 <= ny < ty:
                continue

            if table[nx][ny] == 0 or table[nx][ny] == 2:
                continue

            table[nx][ny] = 2

            puzzle += dfs_table(nx, ny)

        return puzzle
    
    def dfs_board(x, y):
        
        empty = [(x, y)]

        for dx, dy in offset:
            nx, ny = x + dx, y + dy
            
            if not 0 <= nx < gx or not 0 <= ny < gy:
                continue

            if game_board[nx][ny] == 1 or game_board[nx][ny] == 2:
                continue

            game_board[nx][ny] = 2

            empty += dfs_board(nx, ny)

        return empty

    def stadnard(space):
        dx = min([i[0] for i in space])
        dy = min([i[1] for i in space])
        h = max([i[0] for i in space]) - dx + 1
        w = max([i[1] for i in space]) - dy + 1

        grid = [[0]*w for _ in range(h)]

        for x, y in space:
            grid[x-dx][y-dy] = 1

        return grid

        grid = [list(e) for e in zip(*grid[::-1])]

    num = 0
    for i in range(tx):
        for j in range(ty):
            if table[i][j] == 1:
                table[i][j] = 2 
                num += 1
                puzzles.append(stadnard(dfs_table(i, j)))

    for i in range(gx):
        for j in range(gy):
            if game_board[i][j] == 0:
                game_board[i][j] = 2 
                emptys.append(stadnard(dfs_board(i, j)))
                
    result = 0
    is_use = [False]*len(puzzles)
    
    for e in emptys:
        is_empty = True

        for idx, p in enumerate(puzzles):
            if is_use[idx]:
                continue

            cnt = 4
            while cnt:
                if e == p:
                    result += sum([sum(i) for i in e])
                    is_use[idx] = True
                    is_empty = False
                    break
                else:
                    p = [list(e) for e in zip(*p[::-1])]
                    cnt -= 1

            if not is_empty:
                break

    return result
