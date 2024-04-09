input = open(0).readline

node, max_box = map(int,input().split())
box_info = [tuple(map(int,input().split())) for _ in range(int(input()))]

box_info = sorted(box_info, key=lambda x:(x[0],x[1]))

now_box = 0

total_box = 0

from heapq import *

move_box = []

for start, end, boxes in box_info:
    while move_box and move_box[0][0] <= start:
        now_box -= heappop(move_box)[1]

    can_move = min(max_box-now_box, boxes)
    heappush(move_box, (end, can_move))
    now_box += can_move
    total_box += can_move

print(total_box)