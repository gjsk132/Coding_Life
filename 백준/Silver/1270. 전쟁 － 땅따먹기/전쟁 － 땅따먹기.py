input = open(0).readline

lands = int(input())

def war_status():
    sides = {}
    data = list(map(int, input().split()))
    for i in data[1:]:
        if not i in sides:
            sides[i] = 1
        else:
            sides[i] += 1
    
    max_sides = max(sides.values())
    
    if max_sides > (data[0]//2):
        sides_reverse = {v:k for k,v in sides.items()}
        print(sides_reverse.get(max_sides))
    else:
        print("SYJKGW")
        


for i in range(lands):
    war_status()