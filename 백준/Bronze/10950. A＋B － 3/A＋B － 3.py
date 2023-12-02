input = open(0).readline
for i in range(int(input())):
    print(sum(map(int, input().split())))