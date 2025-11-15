grade = input()

result = 0

if '+' in grade:
    result += 0.3
elif '-' in grade:
    result -= 0.3

if 'A' in grade:
    result += 4
elif 'B'in grade:
    result += 3
elif 'C'in grade:
    result += 2
elif 'D'in grade:
    result += 1
    
print(float(result))