input = open(0).readline

N, M = map(int, input().split())
prices = sorted([int(input()) for _ in range(M)])

p = 0
t = 0

for i, price in enumerate(prices):
    cnt = min(N, M-i)
    if price*cnt > t:
        p = price
        t = price*cnt

print(p, t)