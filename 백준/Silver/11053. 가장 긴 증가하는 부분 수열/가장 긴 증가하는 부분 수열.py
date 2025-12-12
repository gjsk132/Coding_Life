input = open(0).readline

N = int(input())

nums = list(map(int, input().split()))

board = [1]*N

max_v = 0


for i in range(N):
    now_v, now_cnt = nums[i], board[i]

    for j in range(i):
        pre_v, pre_cnt = nums[j], board[j]

        
        if now_v > pre_v and pre_cnt+1 > now_cnt:
            now_cnt = pre_cnt+1

    board[i] = now_cnt
    max_v = max(max_v, now_cnt)

print(max_v)