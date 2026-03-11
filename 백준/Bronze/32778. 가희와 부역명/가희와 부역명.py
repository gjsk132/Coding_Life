input = open(0).readline

tmp = input().strip()

if "(" in tmp:
    print("\n".join(tmp[:-1].split(" (")))
else:
    print(tmp)
    print("-")