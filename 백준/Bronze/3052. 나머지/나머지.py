import sys
left = set([])
for i in range(10):
    n = int(sys.stdin.readline())
    left.add(n%42)
print(len(left))