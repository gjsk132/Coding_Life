x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

a = pow((x2-x1), 2) + pow((y2-y1), 2)
b= pow((r1+r2), 2) 

if  a < b:
    print("YES")
else:
    print("NO")