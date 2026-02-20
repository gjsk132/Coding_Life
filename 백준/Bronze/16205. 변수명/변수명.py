input = open(0).readline

num, words = input().split()

w = []

if num == "2":
    w = words.split("_")
else:
    words = words[0].lower()+words[1:]

    p = 0

    for i in range(len(words)):
        if words[i].isupper():
            w.append(words[p].lower()+words[p+1:i])
            p = i

    w.append(words[p].lower()+words[p+1:])

for k, v in enumerate(w):
    if k == 0:
        print(v, end="")
    else:
        print(v[0].upper()+v[1:], end="")
print()
print("_".join(w))
for v in w:
    print(v[0].upper()+v[1:], end="")