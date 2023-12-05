input= open(0).readline

while True:
    a, b = map(int,input().split())
    if a == b == 0:
        break
    print(a+b)