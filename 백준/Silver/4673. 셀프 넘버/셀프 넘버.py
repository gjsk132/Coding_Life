self = [True for i in range(10001)]

for i in range(10000):
    no_self = i
    for j in str(i):
        no_self += int(j)
    if no_self > 10000:
        continue
    self[no_self] = False

for i in range(10000):
    if self[i]:
        print(i)