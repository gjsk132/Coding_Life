from heapq import *
input = open(0).readline

cnt = int(input())
slime = [-plus for plus in map(int,input().split())]
heapify(slime)

score = 0

while (cnt := cnt-1):
    s1, s2 = heappop(slime), heappop(slime)
    heappush(slime, s1+s2)
    score += s1*s2

print(score)