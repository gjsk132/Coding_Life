input = open(0).readline

h, m, s = map(int, input().split())

add_s = int(input())

s += add_s

m += s//60
s %= 60

h += m//60
m %= 60

h %= 24

print(h, m, s)