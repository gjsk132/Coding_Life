input = open(0).readline

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(y):
    return (y%4==0 and not y%100==0 or y%400==0)

year, day = int(input()), int(input())

# index 0부터 시작
day -= 1

# 이번 달에 몇 일까지 있는지 확인 (윤년이면 +1)
day_in_month[1] += int(is_leap_year(year))

answer = 0

for month in range(12):
    for date in range(7):
        today_day = (day + date)%7

        if (date +1) + 28 <= day_in_month[month]:
            answer += 1
    
    day = (day + (day_in_month[month])%7)%7
print(answer)