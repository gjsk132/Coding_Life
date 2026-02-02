input = open(0).readline

contents = input().strip()

pos = 0

NOP = 0

for c in list(contents):
    while c.isupper() and pos%4:
        NOP += 1
        pos += 1
    pos += 1

print(NOP)