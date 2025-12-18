input = open(0).readline

N, M = map(int, input().split())

nums = [i+1 for i in range(N)]

for _ in range(M):
    s, e = map(int, input().split())

    nums[s-1:e] = reversed(nums[s-1:e])
    
print(" ".join(map(str, nums)))