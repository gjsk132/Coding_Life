lines = set()

angle_sum = 0

for i in range(3):
    n = int(input())
    
    angle_sum += n
    
    lines.add(n)
    
if angle_sum == 180:
    if len(lines) == 1:
        print("Equilateral")
    elif len(lines) == 2:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Error")