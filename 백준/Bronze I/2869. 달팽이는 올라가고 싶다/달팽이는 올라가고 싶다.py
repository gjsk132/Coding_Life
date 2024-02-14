up, down, target = map(int,input().split())
gap = up-down

target -= up

print(target//gap + 2 if target%gap else target//gap + 1)