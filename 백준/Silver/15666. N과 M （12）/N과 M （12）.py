from collections import defaultdict

input = open(0).readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

stack = []

check = defaultdict(bool)

def recursion(pre, cnt):
    if cnt == M:
        answer = " ".join(map(str, stack))
        if not check[answer]:
            check[answer] = True
            print(answer) 
        return
    
    for i in range(pre, N):
        stack.append(nums[i])
        recursion(i, cnt+1)
        stack.pop()

recursion(0, 0)