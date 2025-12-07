input = open(0).readline

cnt = int(input())

base = input().strip()

check = [False]*len(base)

for _ in range(cnt-1):

    now = input().strip()

    for k, v in enumerate(now):
        if not base[k] == v:
            check[k] = True

for k, v in enumerate(base):
    if check[k]:
        print("?", end="")
    else:
        print(v, end="")

print()