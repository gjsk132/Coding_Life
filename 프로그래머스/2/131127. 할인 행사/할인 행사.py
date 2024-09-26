def solution(want, number, discount):
    left_shopping_list = {x : y for x, y in zip(want, number)}

    can_sign_up = 0

    for day, dc in enumerate(discount):
        if dc in want:        
            left_shopping_list[dc] -= 1

        if day < 9:
            continue
        elif not day == 9:
            finish_dc = discount[day-10]

            if finish_dc in want:
                left_shopping_list[finish_dc] += 1
        
        left_cnt = sum([max(cnt, 0) for cnt in left_shopping_list.values()])

        if left_cnt == 0:
            can_sign_up += 1

    return can_sign_up