input = open(0).readline

restaurants_cnt = int(input())

flag = False

for _ in range(restaurants_cnt):
    if flag:
        break

    pea_soup = False
    pancakes = False
    
    menus_cnt = int(input())
    
    restaurants_name = input().strip()

    for _ in range(menus_cnt):
        menu_name = input().strip()

        if menu_name == "pea soup":
            pea_soup = True
        elif menu_name == "pancakes":
            pancakes = True
        else:
            continue
        
        if pea_soup and pancakes:
            print(restaurants_name)
            flag = True
            break

if not flag:
    print("Anywhere is fine I guess")