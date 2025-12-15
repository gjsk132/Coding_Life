input = open(0).readline

N, M = map(int, input().split())

nums = [i+1 for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())

    tmp = nums[b-1]
    nums[b-1] = nums[a-1]
    nums[a-1] = tmp

print(" ".join(map(str, nums)))