input = open(0).readline

def answer(length):

    cnt = 0

    now = 0.0

    while now < length:
        now += float(1/(cnt+2))
        cnt += 1
    return cnt

a = 0.0

while (a:=float(input())):
    print(str(answer(a))+" card(s)")