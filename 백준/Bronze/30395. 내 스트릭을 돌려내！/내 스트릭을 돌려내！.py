input = open(0).readline

day = int(input())

solved = list(map(int, input().split()))

answer = 0

last_day_used_strick = -2

def can_use_strick(now):
    return now >= last_day_used_strick + 2

check_day = 0

for today, s in enumerate(solved):
    if s == 0:
        if not can_use_strick(today):
            check_day = 0
            continue
        else:
            last_day_used_strick = today
    else:
        check_day += 1
    
    answer = max(answer, check_day)

print(answer)