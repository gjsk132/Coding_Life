input = open(0).readline

cases = int(input())

def recursion(n, a, b):
    
    cnt = 1
    if (a == b):
        return cnt
    
    val = pow(2, n-1)

    a, b = max(a, b), min(a, b)

    if (a > val):
        a -= val
        
    cnt += recursion(n-1, a, b)

    return cnt

for _ in range(cases):
    n, a, b = map(int, input().split())
    print(recursion(n, a, b))