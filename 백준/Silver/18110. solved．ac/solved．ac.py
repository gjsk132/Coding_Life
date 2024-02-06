input = open(0).readline

people = int(input())
level = sorted([int(input()) for i in range(people)])

gap = int(people*0.15+0.5)
print(0 if not people else int(sum(level[gap:people-(gap)])/(people-2*gap)+0.5))