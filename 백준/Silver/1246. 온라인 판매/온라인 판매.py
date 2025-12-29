input = open(0).readline

N, M = map(int, input().split())

prices = sorted([int(input()) for _ in range(M)])

answer_price = 0
answer_total = 0

for i, price in enumerate(prices):
    cnt = min(N, M-i)

    if price*cnt > answer_total:
        answer_price = price
        answer_total = price*cnt

print(answer_price, answer_total)