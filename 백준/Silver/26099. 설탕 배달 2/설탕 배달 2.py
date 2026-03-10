input = open(0).readline

N = int(input())

offset = [0, 1, 2, 1, 2, 3]
cannot = [4, 7]

print((N//5 + offset[N%5]) if not N in cannot else -1)