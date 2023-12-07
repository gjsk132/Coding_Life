t = int(input())
for i in range(1, t+2):
    if i==t+1:
        print(0)
        break
    n = i + sum(map(int,str(i)))
    if n == t:
        print(i)
        break