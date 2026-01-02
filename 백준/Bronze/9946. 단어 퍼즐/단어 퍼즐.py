from collections import defaultdict

input = open(0).readline

num = 0

while True:
    a = input().strip()
    b = input().strip()

    if a == "END" and b == "END":
        break

    cnt = defaultdict(int)

    num += 1
    for i in a:
        cnt[i] += 1

    for i in b:
        cnt[i] -= 1

    flag = False

    for k, v in cnt.items():
        if not v == 0:
            flag = True
            break

    print(f"Case {num}:", end=" ")
    print("different" if flag else "same")