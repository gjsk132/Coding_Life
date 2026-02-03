input = open(0).readline

sandwich_price, more_money = map(int, input().split())

left_price = sandwich_price - 1023

flag = False

if left_price <= 0:
    print("No thanks")
elif left_price <= more_money:
    left_price_bin, more_money_bin = bin(left_price)[-1::-1], bin(more_money)[-1::-1]

    flag = False

    for k, v in enumerate(list(left_price_bin)):
        if v == 'b' or flag:
            break

        if v == '1' and not more_money_bin[k] == '1':
            flag = True

    if flag:
        print("Impossible")
    else:
        print("Thanks")
    
else:
    print("Impossible")