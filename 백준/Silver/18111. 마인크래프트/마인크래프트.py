input = open(0).readline

N, M, B = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]

min_height, max_height = float("inf"), 0

for row in ground:
    for cell in row:
        min_height = min(min_height, cell)
        max_height = max(max_height, cell)


def calculate_plan(target):

    used_block = 0
    time = 0

    for row in ground:
        for height in row:
            # 1번 경우 : remove
            if (gap:=target-height) < 0:
                time -= gap*2
                used_block += gap
            # 2번 경우 : build
            else:
                time += gap
                used_block += gap
    
    return (time, used_block)

answer_time, answer_height = float('inf'), 0

for n in range(min_height, max_height+1):
    need_time, used_block = calculate_plan(n)

    # too much used block > stop checking
    if used_block > B:
        break
    # save lowest answer > check higher height
    elif need_time < answer_time:
        answer_time, answer_height = need_time, n
    elif need_time == answer_time:
        answer_height = n
        
print(answer_time, answer_height)
