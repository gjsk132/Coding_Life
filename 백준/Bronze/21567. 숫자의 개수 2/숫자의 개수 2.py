input = open(0).readline

A = int(input())
B = int(input())
C = int(input())

cal = A * B * C

nums = [0 for _ in range(10)]

for n in str(cal):
    nums[int(n)] += 1

for n in nums:
    print(n)