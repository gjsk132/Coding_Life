input = open(0).readline

while (text := input().rstrip()) and text != '.':
    
    dq = []
    good = True

    for i in text:
        if i in "([":
            dq.append(i)
        elif i in ")]":
            if not dq or not dq.pop()+i in ["()","[]"]:
                good = False
                break
        
    print("yes" if good and not dq else "no")