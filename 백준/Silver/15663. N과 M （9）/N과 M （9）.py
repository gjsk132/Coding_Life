from collections import defaultdict

input = open(0).readline

N, M = map(int, input().split())

nums = sorted(list(map(int, input().split())))

stack = []

check_dup = [False]*N
check_print = defaultdict(bool)

def recursion(cnt):
    if cnt == M:
        answer = " ".join(map(str, stack))
        if not check_print[answer]:
            check_print[answer] = True
            print(answer) 
        return
    
    for i in range(N):
        if check_dup[i]:
            continue

        stack.append(nums[i])
        check_dup[i] = True

        recursion(cnt+1)

        stack.pop()
        check_dup[i] = False

recursion(0)