input = open(0).readline

basket, order = map(int,input().split())

ball = [0]*(basket+1)

for i in range(order):
    x,y,n = map(int,input().split())
    for j in range(x, y+1):
        ball[j] = n

print(*ball[1:])