input = open(0).readline

MAX_LIMIT = 10**6

prime = [True] * MAX_LIMIT
plist = []

for i in range(2, 1001):
    if prime[i]:
        for j in range(i**2, MAX_LIMIT, i):
            prime[j] = False
        plist.append(i)

while (n := int(input())):
    can = False
    for p in plist:
        if prime[n-p]:
            print("{} = {} + {}".format(n, p, n - p))
            can = True
            break
    if not can:
        print("Goldbach's conjecture is wrong.")