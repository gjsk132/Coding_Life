input = open(0).readline

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

m, d = map(int, input().split())

day_cnt = sum(day_in_month[:m-1]) + d-1

print(date[day_cnt%7])