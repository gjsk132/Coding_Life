input = open(0).readline

student_cnt = int(input())

# id, score
prizes = [[0, 0]]*4

score_table = [list(map(int, input().split())) for _ in range(student_cnt)]

prize_student_id = [0, 0, 0, 0]

for subject_idx in range(4):
    score_table = sorted(score_table, key=lambda x: (x[subject_idx+1], -x[0]))

    prize_student_info = score_table.pop()

    prize_student_id[subject_idx] = prize_student_info[0]

print(" ".join(map(str, prize_student_id)))