dice = list(map(int,open(0).readline().split()))
num = list(set(dice))

if len(num)==1:
    print(10000+num[0]*1000)
elif len(num)==2:
    for i in num:
        dice.remove(i)
    print(1000+dice[0]*100)
else:
    print(max(num)*100)