import sys
sys.setrecursionlimit(10**6)

input = open(0).readline
size = int(input())
num = sorted(list(map(int,input().split())))
goal = int(input())

def find(start,end,target):
    if start >= end:
        return 0
        
    if num[start] + num[end] > target:
        return find(start, end-1, target)
    
    elif num[start] + num[end] < target:
        return find(start+1, end, target)
    
    elif num[start] + num[end] == target:
        return 1+find(start+1,end-1,target)
    
    return
    
print(find(0,size-1,goal))