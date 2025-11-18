input = open(0).readline

M, N = map(int, input().split())

check = [1 for _ in range(N+1)]
check[0], check[1] = 0, 0

num = 2

while num*num <= N:
    if check[num] == 1:
        for not_prime in range(num*2, N+1, num):
            check[not_prime] = 0
    num += 1

for n in range(M, N+1):
    if check[n] == 1:
        print(n)