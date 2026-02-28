input = open(0).readline

no_num = ['0', '1', '2', '3', '5', '6', '8', '9']

num = int(input())

while True:

    flag = True

    for n in str(num):
        if n in no_num:
            flag = False
            break
    
    if flag:
        print(num)
        break
    
    num -= 1