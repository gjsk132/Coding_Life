input = open(0).readline

day, reduce = map(int, input().split())

least_list = list(map(int, input().split()))
increase_list = list(map(int, input().split()))

now_weight = 0
routine_cnt = 0

for least, increase in zip(least_list, increase_list):
    now_weight += increase

    if now_weight < least:
        tmp = least - now_weight
        cnt = tmp//reduce + 1 if tmp%reduce else 0

        routine_cnt -= cnt
        now_weight += cnt*reduce
    
    if routine_cnt < 0:
        routine_cnt = -1
        break

    routine_cnt += (now_weight - least)//reduce
    now_weight = least + (now_weight - least) % reduce
    
print(routine_cnt)