cnt = 0
n = int(input())

while n:
    if n < 100:
        cnt += n
        break
    
    cnt += 1 if (n//100 - (n%100)//10 == (n%100)//10 - n%10) else 0
        
    n -= 1
    
print(cnt)