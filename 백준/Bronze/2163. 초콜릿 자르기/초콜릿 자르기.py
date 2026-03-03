input = open(0).readline

N, M = map(int, input().split())

print(N-1 + N*(M-1))