n = int(input())
x,y = str(n) if n >= 10 else ['0',n]
x, y = int(x), int(y)

cnt = 0
while True:
    x, y = y, x+y
    y %= 10
    cnt += 1
    if x*10+y == n:
        break
print(cnt)