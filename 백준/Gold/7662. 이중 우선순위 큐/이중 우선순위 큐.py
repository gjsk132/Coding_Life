import heapq as hq
from collections import defaultdict

input = open(0).readline

cases = int(input())

for _ in range(cases):
    commands = int(input())
    nums = defaultdict(int)
    nums_min = []
    nums_max = []
    
    hq.heapify(nums_min)
    hq.heapify(nums_max)

    for _ in range(commands):
        c, n = input().split()
        n = int(n)

        if c == "I":
            nums[n] += 1
            hq.heappush(nums_min, n)
            hq.heappush(nums_max, -n)
            continue
        
        if not nums_min or not nums_max:
           continue

        if n == 1:
            while nums_max:
                tmp = hq.heappop(nums_max)
                if nums[-tmp] == 0:
                    continue
                
                nums[-tmp] -= 1
                break

        else:
            while nums_min:
                tmp = hq.heappop(nums_min)
                if nums[tmp] == 0:
                    continue

                nums[tmp] -= 1
                break

    answer_min, answer_max = 0, 0
    flag = False

    while nums_max:
        answer_max = hq.heappop(nums_max)
        if nums[-answer_max] == 0:
            continue
        
        flag = True
        break
    
    while nums_min:
        answer_min = hq.heappop(nums_min)
        if nums[answer_min] == 0:
            continue

        flag = flag and True
        break

    if flag:
        print(-answer_max, answer_min)
    else:
        print("EMPTY")