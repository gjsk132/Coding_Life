input = open(0).readline

cnt, favor_num = map(int, input().split())

towers_height = list(map(int, input().split()))

answer = float('inf')

for ti in range(cnt):
    minute = 0

    if towers_height[ti]-ti*favor_num < 1:
        continue

    for i, th in enumerate(towers_height):
        if not towers_height[ti]+(i-ti)*favor_num == th:
            minute += 1

    answer = min(answer, minute)

print(answer)