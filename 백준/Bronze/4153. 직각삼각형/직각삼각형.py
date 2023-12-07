import sys
while True:
    a,b,c = map(int, sys.stdin.readline().split())
    if a==b==c==0:
        break
    print("right" if (a*a+b*b+c*c-2*max(a,b,c)**2) == 0 else "wrong")