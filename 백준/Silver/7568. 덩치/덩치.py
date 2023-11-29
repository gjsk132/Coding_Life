input = open(0).readline
people = int(input())
size = []

for i in range(people):
    size.append(list(map(int, input().split())))

for i in range(people):
    rank = 1
    for j in range(people):
        if i == j:
            continue
        elif size[i][0] < size[j][0] and size[i][1] < size[j][1]:
            rank += 1
            
    print(rank, end =" ")