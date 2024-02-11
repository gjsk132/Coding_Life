people = int(input())

state = sorted([(x,y) for x, y in zip(map(int,input().split()), map(int,input().split()))])

max_happy = [0 for _ in range(100)]

for hp, happy in state:
    for i in reversed(range(hp, 100)):
        max_happy[i] = max(max_happy[i], max_happy[i-hp]+happy)
        
print(max_happy[-1])