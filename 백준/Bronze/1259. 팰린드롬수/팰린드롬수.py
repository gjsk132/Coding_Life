while True:
    n = input()
    if n == '0':
        break
    print("yes" if n=="".join(reversed(n)) else "no")