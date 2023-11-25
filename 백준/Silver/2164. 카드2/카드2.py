from collections import deque

cnt = int(open(0).readline())
nums = [i+1 for i in range(cnt)]

deq = deque(nums)

while len(deq) != 1:
    deq.popleft()
    deq.append(deq.popleft())
    
print(deq[0])