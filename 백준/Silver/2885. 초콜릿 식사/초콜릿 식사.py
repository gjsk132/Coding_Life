input = open(0).readline

eat = int(input())

choco = 1
while choco < eat:
    choco *= 2

print(choco, end=" ")

cnt = -1

while choco and eat:
    eat -= choco if eat >= choco else 0
    choco //= 2
    cnt += 1
    
print(cnt)