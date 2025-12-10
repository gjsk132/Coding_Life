input = open(0).readline

N, M = map(int, input().split())

stack = []

def recursion(pre, cnt):
    if cnt == M:
        print(" ".join(map(str, stack)))
        return
    
    for i in range(pre, N+1):
        stack.append(i)
        recursion(i, cnt+1)
        stack.pop()

recursion(1, 0)