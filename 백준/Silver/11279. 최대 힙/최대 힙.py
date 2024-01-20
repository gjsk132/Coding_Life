import heapq
input = open(0).readline
nlist = []

for i in range(int(input())):
    num = int(input())
    if num:
        heapq.heappush(nlist, -num)
    else:
        print(-heapq.heappop(nlist) if nlist else 0)