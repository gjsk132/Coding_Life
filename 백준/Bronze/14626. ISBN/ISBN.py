input = open(0).readline

ISBN = input().strip()

check = 0
lost_pos = 0

for idx, num in enumerate(ISBN):
    if num == "*":
        lost_pos = idx
        continue

    n = int(num)
    
    if idx%2:
        check += 3*n
    else:
        check += n


lost = (10 - check%10)%10

if lost_pos%2:
    while lost%3:
        lost += 10
    lost //= 3

print(lost)