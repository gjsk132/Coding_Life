input = open(0).readline
num = input().strip()
string = input().strip()
total = 0
for k,v in enumerate(string):
    total += (ord(v)-96) * 31**k
print(total%1234567891)