alpha = [0]*26
word = input()
for i in range(26):
    alpha[i] = word.find(chr(ord('a')+i))

print(*alpha)