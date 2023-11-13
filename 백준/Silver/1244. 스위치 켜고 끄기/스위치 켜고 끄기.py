input = open(0).readline

switch = int(input())
status = list(map(int, input().split()))
people = int(input())

for i in range(people):
    gender, num = map(int, input().split())
    
    if gender == 1:
        for j in range(num-1, switch, num):
            status[j] ^= 1
        
    elif gender == 2:
        status[num-1] ^= 1
        left = num-2;
        right = num;
        while  left>-1 and right<switch and status[left] == status[right]:
            status[left] ^= 1
            status[right] ^= 1
            left -= 1;
            right += 1;
    
cnt = 0
for i in status[0:]:
    cnt += 1
    print(i, end=' ')    
    if cnt == 20:
        print()
        cnt = 0