from collections import defaultdict

num = defaultdict(int)

for i in input().upper():
    num[i] += 1

high = max(num.values())
dup = 0

for k, v in zip(num.keys(),num.values()):
    if v == high:
        dup += 1
        result = k

print(result if dup == 1 else "?")