input = open(0).readline

n = int(input())

target = [int(input()) for _ in range(n)]
cnt_correct = 0

answer = []

stack = []
top = -1

for num in range(1, n+1):
    
    stack.append(num)
    top += 1
    answer.append("+")

    while stack[top] == target[cnt_correct]:
        stack.pop()
        top -= 1
        cnt_correct += 1
        answer.append("-")

        if top < 0:
            break

if cnt_correct == n:
    for a in answer:
        print(a)
else:
    print("NO")