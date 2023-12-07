for i in range(int(input())):
    h,w,n = map(int, input().split())
    print((n%h if n%h != 0 else h)*100+(n//h+1 if n%h != 0 else n//h))