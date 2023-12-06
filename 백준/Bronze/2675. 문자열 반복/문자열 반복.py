import sys
for i in range(int(sys.stdin.readline())):
    n, m = sys.stdin.readline().split()
    for i in m:
        print(int(n)*i, end="")
    print()