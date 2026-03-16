input = open(0).readline

n, l = map(int, input().split())

red, blue, green = 0, 0, 0

for _ in range(n):
    input()

for _ in range(l):
    _s, _e, color = input().split()

    if color == "R":
        red += 1
    elif color == "B":
        blue += 1
    else:
        green += 1

if (red == blue):
    print("jhnah917" if green%2 else "jhnan917")
else:
    print("jhnah917" if red > blue else "jhnan917")