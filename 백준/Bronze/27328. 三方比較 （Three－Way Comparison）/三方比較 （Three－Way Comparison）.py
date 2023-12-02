input = open(0).readline
n1 = int(input())
n2 = int(input())
print(int(n1 > n2) if n1 >= n2 else -1)