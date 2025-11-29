import sys
sys.setrecursionlimit(10**7)

input = open(0).readline

K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]

def binery_search(start, end):
    if start > end:
        return end

    mid = (start+end)//2

    cnt = sum([l//mid for l in lines])

    if cnt < N:
        return binery_search(start, mid-1)
    else:
        return binery_search(mid+1, end)

print(binery_search(1, sum(lines)//N))