input = open(0).readline


n = int(input())

target = [int(input()) for _ in range(n)]
cnt_correct = 0

answer = []

tmp = []
top = -1

for num in range(1, n+1):
    
    tmp.append(num)
    top += 1
    answer.append("+")

    while tmp[top] == target[cnt_correct]:
        
        tmp.pop()
        top -= 1
        cnt_correct += 1
        answer.append("-")

        if cnt_correct > n:
            break

        if top < 0:
            break

if cnt_correct == n:
    for a in answer:
        print(a)
else:
    print("NO")