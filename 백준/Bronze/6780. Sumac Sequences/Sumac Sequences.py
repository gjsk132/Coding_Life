input = open(0).readline

a, b = int(input()), int(input())

cnt = 2

while a >= b:
    tmp = b
    b = a - b
    a = tmp
    cnt += 1

print(cnt)