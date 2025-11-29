input = open(0).readline

N, target = map(int, input().split())

nums = sorted(list(map(int, input().split())))

print(nums[target-1])