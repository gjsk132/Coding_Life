input = open(0).readline

answer = [0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]

for i in range(int(input())):
    num = int(input())
    print(answer[num])