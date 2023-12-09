while True:
    n = input()
    if n == '0':
        break
    if n == "".join(reversed(n)):
        print("yes")
    else:
        print("no")