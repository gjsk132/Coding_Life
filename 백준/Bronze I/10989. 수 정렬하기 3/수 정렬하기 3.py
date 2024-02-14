input = open(0).readline

num = [0 for _ in range(10001)]

for i in range(int(input())):
    num[int(input())] += 1
    
for k, i in enumerate(num):
    for _ in range(i):
        print(k)