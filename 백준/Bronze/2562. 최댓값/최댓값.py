import sys
high, index = 0, 0
for i in range(9):
    n = int(sys.stdin.readline())
    if high < n:
        high = n
        index = i
print(high)
print(index+1)