input = open(0).readline

coin = []

coins, target = map(int,input().split())

for i in range(coins):
    if (n:=int(input())) <= target:
        coin.append(n)

cnt = 0

for i in reversed(coin):
    if target >= i:
        cnt += target//i
        target %= i
    
print(cnt)