input = open(0).readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

check = [False]*N
stack = []

def recursion(cnt):
    if cnt == M:
        print(" ".join(map(str, stack)))
        return
    
    for i in range(N):
        if check[i]:
            continue

        stack.append(nums[i])
        check[i] = True

        recursion(cnt+1)
        
        stack.pop()
        check[i] = False

recursion(0)