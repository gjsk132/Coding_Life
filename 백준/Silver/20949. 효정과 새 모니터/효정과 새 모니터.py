input = open(0).readline

N = int(input())

monitors = [list(map(int, input().split()))+[i+1] for i in range(N)]

for m in sorted(monitors, key=lambda x: x[0]**2+x[1]**2, reverse=True):
    print(m[2])