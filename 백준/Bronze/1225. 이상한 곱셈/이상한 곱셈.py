input = open(0).readline

A, B = input().split()

print(sum(map(int, list(A)))*sum(map(int, list(B))))