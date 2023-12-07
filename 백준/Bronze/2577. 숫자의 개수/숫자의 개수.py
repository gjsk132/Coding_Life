import sys
from collections import defaultdict
num = defaultdict(int)
result = 1 

for i in range(3):
    result *= int(input())

for i in str(result):
    num[i] += 1

for i in range(10):
    print(num[str(i)])