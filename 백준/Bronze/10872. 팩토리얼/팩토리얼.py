input = open(0).readline

cnt = int(input())

answer = 1

for i in range(2, cnt+1):
    answer *= i

print(answer)