input = open(0).readline
num = int(input())

cnt = 1

while num > cnt:
    num -= cnt
    cnt += 1

if (cnt%2==1):
    print("{}/{}".format(cnt-num+1, num))
else:
    print("{}/{}".format(num, cnt-num+1))