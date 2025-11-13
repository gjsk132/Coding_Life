input = open(0).readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

need_t = 0

for s in sizes:
    need_t += s//T
    need_t += 1 if s%T else 0

print(need_t)

print(N//P, N%P)