def solution(maps):
    
    answer = []    
    offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    memo = [[int(i) if not i == 'X' else 0 for i in row] for row in maps]

    h, w = len(maps), len(maps[0])

    def bfs(x, y):
        total = memo[x][y]
        memo[x][y] = 0

        dq = [(x, y)]

        while dq:
            x, y = dq.pop()

            for dx, dy in offset:
                px = x + dx
                py = y + dy

                if not 0 <= px < h or not 0 <= py < w:
                    continue

                if (value := memo[px][py]) == 0:
                    continue

                total += value
                memo[px][py] = 0
                dq.append((px, py))

        return total

    for x in range(h):
        for y in range(w):
            if memo[x][y] == 0:
                continue
            
            answer.append(bfs(x, y))

    if not answer:
        answer.append(-1)

    return sorted(answer)