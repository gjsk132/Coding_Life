total = 0

for i in range(1, (n:=int(input()))+1):
    if i > n//i:
        break
    elif n%i == 0:
        total += (i + (n//i)) if i!=n//i else i

print(total*5-24)