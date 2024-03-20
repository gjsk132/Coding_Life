num = int(input())
i = 2

while num > 1:
    if not num%i == 0:
        i += 1
        continue
    
    num /= i
    print(i)