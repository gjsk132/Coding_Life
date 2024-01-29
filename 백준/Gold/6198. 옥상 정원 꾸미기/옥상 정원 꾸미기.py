input = open(0).readline
n = int(input())
building = [[int(input()),0] for _ in range(n)]
cnt = 0

for i in range(n):
    top = n - i - 1
    while top:
        if building[top][0] < building[top-1][0]:
            building[top-1][1] += building[top][1] + 1
            cnt += building[top][1]
            building.pop(top)
            break
        else:
            top -= 1

while building:
    a, b = building.pop()
    cnt += b

print(cnt)