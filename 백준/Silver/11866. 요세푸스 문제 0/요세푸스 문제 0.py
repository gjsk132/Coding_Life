from collections import deque

input = open(0).readline

N, K = map(int,input().split())

answer = []

nums = deque([i+1 for i in range(N)])

pos = 1

while nums:
    n = nums.popleft()
    
    if not pos%K == 0:
        nums.append(n)
    else:
        answer.append(str(n))

    pos += 1

print("<", end="")
print(", ".join(answer), end=">")