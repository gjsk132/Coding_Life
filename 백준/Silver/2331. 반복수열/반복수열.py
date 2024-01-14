A, P = map(int,input().split())

nums = []

while not A in nums:
    nums.append(A)
    n = 0
    for i in str(A):
        n += int(i)**P
    A = n

print(nums.index(A))