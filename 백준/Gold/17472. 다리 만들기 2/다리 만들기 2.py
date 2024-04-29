from collections import deque, defaultdict
from heapq import *

input = open(0).readline

height, width = map(int,input().split())

country = [list(map(int,input().split())) for _ in range(height)]

offset = [(0,1),(1,0),(0,-1),(-1,0)]


# 각 섬의 pos 찾기

pos_land = deque([])

def check_land(x, y, num):
    dq = deque([(x,y)])
    country[x][y] = num

    while dq:
        x, y = dq.popleft()
        for px, py in offset:
            nx = x+px
            ny = y+py
            if nx < 0 or nx == height or ny < 0 or ny == width or not country[nx][ny] == 1:
                continue
            dq.append((nx, ny))
            country[nx][ny] = num

for k1, v1 in enumerate(country):
    for k2, v2 in enumerate(v1):
        if v2==1:
            check_land(k1, k2, len(pos_land)+2)
            pos_land.append((k1, k2))

cnt_land = len(pos_land)


# 섬에서 다른 섬까지의 거리를 heapq에 저장

limit = 10

distance = [[limit for i in range(cnt_land)] for _ in range(cnt_land)]

def check_distance(x, y, num):
    dq = deque([(x,y)])
    while dq:
        x, y = dq.popleft()
        for px, py in offset:
            nx = x+px
            ny = y+py

            if nx < 0 or nx == height or ny < 0 or ny == width or country[nx][ny] == -num:
                continue
            if country[nx][ny] == num:
                dq.append((nx, ny))
                country[nx][ny] = -num
                continue

            dist = 0

            while True:
                nx += px
                ny += py

                if nx < 0 or nx == height or ny < 0 or ny == width:
                    break

                if not (c:=country[nx][ny]) == 0:
                    if (absc := abs(c)-2) <= (n := num-2) or dist < 1:
                        break

                    
                    distance[n][absc] = min(distance[n][absc], dist+1) # 섬을 확인하기 위해 +2한 것을 다시 빼준다.
                    distance[absc][n] = min(distance[absc][n], dist+1)
                    break
                    
                dist += 1

while pos_land:
    land_x, land_y = pos_land.popleft()
    check_distance(land_x, land_y, country[land_x][land_y])


# 가장 작은 다리 구하기

visited_land = [False]*(cnt_land)
visited_land[0] = True

total_length = 0

for _ in range(cnt_land-1):

    min_index = 0
    min_length = 10

    for i, visit in enumerate(visited_land):
        if not visit:
            continue

        for j, length in enumerate(distance[i]):
            if not length%10 or visited_land[j]:
                continue
            
            if length < min_length:
                min_length = length
                min_index = j
    
    if min_length == 10:
        break

    visited_land[min_index] = True
    total_length += min_length

print(total_length if all(visited_land) else -1)