input = open(0).readline

limit = 123456*2 + 1
prime = [1]*limit
prime[0], prime[1] = 0, 0

for i in range(2, 10**3):
    if prime[i]:
        for j in range(i*2, limit, i):
            prime[j] = 0

#prefix sum
for i in range(limit-1):
    prime[i+1] += prime[i]


while (n:=int(input())):
    print(prime[2*n]-prime[n])