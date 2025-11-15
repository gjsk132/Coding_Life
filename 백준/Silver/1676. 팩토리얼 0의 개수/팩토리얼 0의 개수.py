input = open(0).readline

N = int(input())

cnt_2 = 0
cnt_5 = 0

for i in range(1, N+1):
    tmp = i
    while not tmp%2:
        cnt_2 += 1
        tmp //= 2
    while not tmp%5:
        cnt_5 += 1
        tmp //= 5

print(min(cnt_2, cnt_5))