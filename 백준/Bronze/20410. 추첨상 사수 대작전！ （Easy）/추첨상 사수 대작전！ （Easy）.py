input = open(0).readline

m, seed, x_1, x_2 = map(int, input().split())

flag = False

for a in range(m):
    if flag:
        break
    for c in range(m):
        if x_1 == (a*seed+c)%m and x_2 ==(a*x_1+c)%m:
            flag = True
            print(a, c)
            break