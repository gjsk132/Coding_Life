input = open(0).readline

N, time = map(int, input().split())

min_price = float('inf')
idx = 0

for i in range(N):
    initial_price, period, add_price = map(int, input().split())

    cnt = (time//period + (0 if time%period else -1))

    need_money = initial_price + (cnt*(cnt+1))//2 *add_price
    if min_price > need_money:
        min_price = need_money
        idx = i + 1

print(idx, min_price)