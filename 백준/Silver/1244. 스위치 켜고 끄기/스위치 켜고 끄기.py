input = open(0).readline
cnt = int(input())
state = list(map(int,input().split()))

for i in range(int(input())):
    gender, num = map(int,input().split())
    
    if gender == 1:
        for i in range(num-1,cnt,num):
            state[i] ^= 1
    else:
        left = num-2
        right = num
        state[num-1] ^= 1
        while left > -1 and right < cnt and state[left]==state[right]:
            state[left] ^= 1
            state[right] ^= 1
            left -= 1
            right += 1

for k, v in enumerate(state):
    print(v, end=" ")
    if not (k+1)%20:
        print()