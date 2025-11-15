input = open(0).readline

n = 0
cnt = 0
target = int(input())

while cnt != target:
    if '666' in str(n):
        cnt += 1
    n += 1

print(n-1)