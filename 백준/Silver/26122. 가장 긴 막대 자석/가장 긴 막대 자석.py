input = open(0).readline

total_length = int(input())

magnet_info = [0]

now = "N"

for m in list(input().strip()):
    if m == now:
        magnet_info[-1] += 1
    else:
        now = m
        magnet_info.append(1)

answer = 0

for i in range(len(magnet_info)-1):
    answer = max(answer, min(magnet_info[i:i+2])*2)

print(answer)