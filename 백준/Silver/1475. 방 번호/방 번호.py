room_number = open(0).readline().strip()
room_number = room_number.replace('9', '6')

cnt = [0 for i in range(10)]

for i in room_number:
    cnt[int(i)] += 1

if cnt[6]%2 == 0:
    cnt[6] = cnt[6]//2
else:
    cnt[6] = (cnt[6]//2) + 1
    
print(max(cnt))