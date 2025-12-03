import heapq as hq
from collections import defaultdict

input = open(0).readline

ladder_cnt, snake_cnt = map(int, input().split())

move = defaultdict(int)

for _ in range(ladder_cnt+snake_cnt):
    s, e = map(int, input().split())
    move[s] = e

poses = [(0, -1)]
hq.heapify(poses)

board = [-1 for _ in range(101)]
board[0] = 0

while poses:
    cnt, pos = hq.heappop(poses)
    pos = -pos
    if pos == 100:
        print(cnt)
        break

    for dice in range(6, 0, -1):
        next_pos = pos + dice

        if next_pos > 100:
            continue

        if not board[next_pos] == -1:
            continue

        if move[next_pos] == 0:
            board[next_pos] = cnt+1
            hq.heappush(poses, (cnt+1, -next_pos))
        else:
            board[next_pos] = cnt+1
            move_pos = move[next_pos]
            board[move_pos] = cnt+1
            hq.heappush(poses, (cnt+1, -move_pos))