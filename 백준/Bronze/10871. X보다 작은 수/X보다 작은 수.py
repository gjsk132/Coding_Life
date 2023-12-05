import sys
n, x = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
print(*[i for i in num if i < x])