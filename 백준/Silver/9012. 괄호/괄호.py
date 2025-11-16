input = open(0).readline

def check_VPS(PS):
    while "()" in PS:
        PS = PS.replace("()", "")
    
    if PS == "":
        return True
    else:
        return False

N = int(input())

for _ in range(N):
    now_PS = input().strip()

    if check_VPS(now_PS):
        print("YES")
    else:
        print("NO")