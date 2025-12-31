input = open(0).readline

word = input().strip()

word_num = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

sec = 0

for s in word:
    for idx, wn in enumerate(word_num):
        if s in wn:
            sec += idx + 3
            break

print(sec)