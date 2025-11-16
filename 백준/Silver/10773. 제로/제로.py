input = open(0).readline

K = int(input())

moneys = []

for _ in range(K):
    m = int(input())

    if m == 0:
        moneys.pop()
    else:
        moneys.append(m)

print(sum(moneys))