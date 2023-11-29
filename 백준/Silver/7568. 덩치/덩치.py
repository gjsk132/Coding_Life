from collections import deque

input = open(0).readline
people = int(input())
deq = deque([])

for i in range(people):
    deq.append(list(map(int, input().split())))

for i in range(people):
    now = deq.popleft()
    rank = 1
    for j in deq:
        if now[0] < j[0] and now[1] < j[1]:
            rank += 1
    deq.append(now)
    print(rank, end=" ")