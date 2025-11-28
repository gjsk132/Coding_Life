input = open(0).readline

sing_num = 1

answer = 0

left = int(input())

while not left == 0:
    if sing_num > left:
        sing_num = 1
        continue
    
    left -= sing_num
    sing_num += 1
    answer += 1
    
print(answer)