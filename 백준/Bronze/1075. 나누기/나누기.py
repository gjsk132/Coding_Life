input = open(0).readline

N, M = int(input()), int(input())

tmp = (N//100*100)%M
answer = (M-tmp)%M

print(f"{answer:02d}")