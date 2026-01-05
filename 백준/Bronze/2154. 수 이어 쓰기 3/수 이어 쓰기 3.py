input = open(0).readline

num = input().strip()

nums = "".join(str(i) for i in range(1, int(num)+1))

print(nums.index(num)+1)