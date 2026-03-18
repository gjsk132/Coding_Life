from heapq import *

input = open(0).readline

lines = int(input())

lines_info = [tuple(map(int, input().split())) for _ in range(lines)]

heapify(lines_info)

total_length = 0

while lines_info:
    start, end = heappop(lines_info)

    # 선이 하나 남았을 때 or 다음 선과 겹치지 않을 때
    if not lines_info or end < lines_info[0][0]:
        total_length += end - start
        continue

    _, next_end = heappop(lines_info)

    # 겹치는 선을 합쳐서 heap에 다시 넣음
    heappush(lines_info, (start, max(end, next_end)))

print(total_length)