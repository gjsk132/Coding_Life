a, b = map(int,input().split())

lmc_gcd = a*b

while (a := a%b) if a > b else (b := b%a):
    continue

gcd = max(a, b)
print(gcd)
print(lmc_gcd//gcd)