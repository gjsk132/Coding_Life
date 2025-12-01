input = open(0).readline

N, M = int(input()), int(input())

target = "I" + "OI"*N

S = input().strip()

cnt = 0

for i in range(0, M-2*N):
    if S[i:i+2*N+1] == target:
        cnt += 1

print(cnt)