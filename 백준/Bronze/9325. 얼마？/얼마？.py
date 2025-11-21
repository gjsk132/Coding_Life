input = open(0).readline

def car_price_with_all_options(c_price, os_cnt):
    total = car_price

    for _ in range(options_cnt):
        o_cnt, o_price = map(int, input().split())

        total += o_cnt * o_price
    
    return total

cases = int(input())

for _ in range(cases):
    car_price = int(input())
    options_cnt = int(input())

    print(car_price_with_all_options(car_price, options_cnt))