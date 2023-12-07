t = int(input())
for i in range(1, t+2):
    if i==t+1:
        print(0)
        break
    n = i
    for j in str(i):
        n += int(j)
    if n == t:
        print(i)
        break