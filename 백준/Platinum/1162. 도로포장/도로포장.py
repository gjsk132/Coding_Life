from heapq import *
input = open(0).readline

city, road, paving = map(int,input().split())

board = [[] for _ in range(city+1)]
min_dist = [[float('inf')]*(city+1) for _ in range(paving+1)]

for _ in range(road):
    n1, n2, w = map(int,input().split())
    board[n1].append((n2, w))
    board[n2].append((n1, w))

hq = [(0, 1, 0)] # dist, next node, layer

if paving < road:
    while hq:
        dist, now, layer = heappop(hq)

        if min_dist[layer][now] < dist:
            continue

        for nxt, w in board[now]:

            if min_dist[layer][nxt] > dist + w:
                min_dist[layer][nxt] = dist + w
                heappush(hq, (dist + w, nxt, layer))
            
            if layer == paving:
                continue

            if min_dist[layer+1][nxt] > dist:
                min_dist[layer+1][nxt] = dist
                heappush(hq, (dist, nxt, layer+1))
    print(min_dist[-1][-1])
else:
    print(0)