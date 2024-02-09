from collections import defaultdict

input = open(0).readline

words = defaultdict(int)

for i in range(int(input())):
    words[input().strip()] += 1
    
max_cnt = max(words.values())

max_words = []

for key, value in words.items():
    if value == max_cnt:
        max_words.append(key)
        
print(min(max_words))