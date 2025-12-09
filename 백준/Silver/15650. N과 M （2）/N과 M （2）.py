input = open(0).readline

N, M = map(int, input().split())

stack = []

def recursion(pre, cnt):
    # base
    if cnt == M:
        print(" ".join(map(str, stack)))
        return
    
    for i in range(pre+1, N+1):
        stack.append(i)
        recursion(i, cnt+1)
        stack.pop()

recursion(0, 0)