input = open(0).readline

keyboard = {0:'`1QAZ', 1:'2WSX', 2:'3EDC', 3:'4RFV5TGB', 4:'6YHN7UJM', 5:'8IK,', 6:'9OL.', 7:"0P;/-['=]"}

input_cnt = [0 for _ in range(8)]

input_k = input().strip()

for i in input_k:
    for k, v in keyboard.items():
        if i in v:
            input_cnt[k] += 1
            break

for i in input_cnt:
    print(i)