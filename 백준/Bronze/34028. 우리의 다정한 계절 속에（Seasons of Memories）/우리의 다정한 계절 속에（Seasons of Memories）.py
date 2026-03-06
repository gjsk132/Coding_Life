input = open(0).readline

y, m, d = map(int, input().split())

sy, sm, sd = 2015, 1, 16

answer = (y - sy)*4 + 1

if m > 11:
    answer += 4
elif m > 8:
    answer += 3
elif m > 5:
    answer += 2
elif m > 2:
    answer += 1

print(answer)