input = open(0).readline

N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]

dots.sort(key = lambda x: (x[1], x[0]))

for d in dots:
    print(d[0], d[1])