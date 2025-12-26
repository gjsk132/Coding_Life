input = open(0).readline

def check_versus():
    rounds = int(input())
    if not rounds:
        return "end"

    marks = list(map(int, input().split()))
    letis = list(map(int, input().split()))

    mark_score = sum(marks)
    leti_socre = sum(letis)

    def check_bonus_index(datas):
        t_i = -1
        t_v = 0
        t_c = 1

        for i, v in enumerate(datas):
            if v == t_v:
                t_c += 1
                if t_c == 3:
                    t_i = i
                    break
            else:
                t_v = v
                t_c = 1

        return float('inf') if t_i == -1 else t_i

    marks_bonus_index = check_bonus_index(marks)
    letis_bonus_index = check_bonus_index(letis)

    if marks_bonus_index < letis_bonus_index :
        mark_score += 30
    elif marks_bonus_index > letis_bonus_index:
        leti_socre += 30
    
    if mark_score > leti_socre:
        return "M"
    elif mark_score < leti_socre:
        return "L"
    else:
        return "T"


while True:
    answer = check_versus()
    if answer == "end":
        break

    print(answer)