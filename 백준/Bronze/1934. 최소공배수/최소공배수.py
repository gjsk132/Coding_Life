input = open(0).readline

cases = int(input())

for _ in range(cases):
    a, b = map(int, input().split())

    max_n, min_n = max(a, b), min(a, b)

    while (remain:=max_n%min_n):
        max_n, min_n = min_n, remain
    
    gcd = min_n

    print(a*b//gcd)