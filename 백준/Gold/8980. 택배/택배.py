input = open(0).readline

node, max_box = map(int,input().split())
box_info = [tuple(map(int,input().split())) for _ in range(int(input()))]

box_info = sorted(box_info, key=lambda x:(x[1],x[0]))

left_move = [max_box]*(node+1)

total_box = 0

for start, end, boxes in box_info:

    can_move = min(min(left_move[start:end]), boxes)
    for idx in range(start,end):
        left_move[idx] -= can_move
    total_box += can_move

print(total_box)