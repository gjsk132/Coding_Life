input = open(0).readline

while n:=int(input()):
    a1, a2, a3 = map(int, input().split())

    if a3+a1 == a2+a2:
        d = a2-a1
        print((n)*(2*a1+(n-1)*d)//2)
        
    else:
        r = a2//a1
        print((a1)*(pow(r, n)-1)//(r-1))