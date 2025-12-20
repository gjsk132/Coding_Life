input = open(0).readline

start_date, add_day = input().split()

m_in_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

y, m, d = map(int, start_date.split("-"))

d += int(add_day)-1

while True:
    is_leap_year = (y%4 == 0 and y%100 != 0) or y%400 == 0

    sub_d = m_in_days[m] + (1 if m == 2 and is_leap_year else 0)

    if d <= sub_d:
        break
    else:
        d -= sub_d
        m += 1

        if m > 12:
            m = 1
            y += 1

print(f"{y:04d}-{m:02d}-{d:02d}")