input = open(0).readline

score = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}

answer = 0.0
cnt = 0

for _ in range(20):
    name, grade, value = input().split()
    if value == "P":
        continue
    
    grade = float(grade)
    answer += score[value]*grade
    cnt += grade

print(answer/cnt)