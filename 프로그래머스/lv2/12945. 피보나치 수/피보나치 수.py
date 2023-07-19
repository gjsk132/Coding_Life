def solution(n):
    
    a = 0
    b = 1
    
    if (n ==0):
        return a
    if (n==1):
        return b
    
    for i in range(n-1):
        c = a + b
        a = b
        b = c
         
    return c%1234567