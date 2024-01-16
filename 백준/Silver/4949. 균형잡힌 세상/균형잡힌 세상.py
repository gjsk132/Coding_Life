from collections import deque

while True:
    text = input()
    if text == ".":
        break
    
    dq = deque()
    good = True

    for i in text:
        if i in "([":
            dq.append(i)
        elif i in ")]":
            if not dq:
                good = False
                break
            
            op = dq.pop()
            if (op=="(" and i ==")") or (op=="[" and i =="]"):
                continue
            
            good = False
            break
        
    print("yes" if good and (not dq) else "no")