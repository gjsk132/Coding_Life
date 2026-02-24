input = open(0).readline

seats = [0]*101

peoples = int(input())

reject_cnt = 0

for pos in list(map(int, input().split())):
    if not seats[pos]:
        seats[pos] = 1
    else:
        reject_cnt += 1

print(reject_cnt)