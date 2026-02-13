from collections import defaultdict

input = open(0).readline

people, orders = map(int, input().split())

people_table = []

for idx in range(people):
    people_table.append(list(map(int, input().split())))

people_table.sort(key=lambda x: (x[0], x[1]))

time_price = defaultdict(int)

for _ in range(orders):
    t, p = map(int, input().split())

    time_price[t] += p

time_price = sorted([[k, v] for k, v in time_price.items()])

total_price = 0

people_num = 0
finish_flag = False

for t, p in time_price:
    
    flag = False

    while not (people_table[people_num][0] <= t and t<= people_table[people_num][1]):
        people_num += 1
        
        if people_num == people:
            finish_flag = True
            break

        if t < people_table[people_num][0]:
            flag = True
            break

    if finish_flag:
        break

    if flag:
        continue
    
    total_price += p

print(total_price/people)