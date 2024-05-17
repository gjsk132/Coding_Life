input = open(0).readline

x = []
y = []

for i in range(3):
    nx, ny = map(int, input().split())
    if nx in x:
        x.remove(nx)
    else:
        x.append(nx)
    if ny in y:
        y.remove(ny)
    else:
        y.append(ny)

print(x[0], y[0])