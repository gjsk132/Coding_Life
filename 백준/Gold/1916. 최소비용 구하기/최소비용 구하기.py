import heapq as hq
from collections import defaultdict

input = open(0).readline

node, line = int(input()), int(input())

board = defaultdict(dict)

for _ in range(line):
    s, e, c = map(int, input().split())
    
    if not e in board[s].keys():
        board[s][e] = c
    else:
        board[s][e] = min(board[s][e], c)

start, target = map(int, input().split())

min_dist = [float('inf') for _ in range(node+1)]

a = [(0, start)]

hq.heapify(a)

while a:
    cost, node = hq.heappop(a)

    for next_n, next_c in board[node].items():
        if min_dist[next_n] <= cost+next_c:
            continue

        min_dist[next_n] = cost+next_c
        hq.heappush(a, (cost+next_c, next_n))

print(min_dist[target])