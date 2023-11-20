input = open(0).readline
n = int(input())
for i in range(n):
    
    grade = list(map(int,input().split()))
    grade = sorted(grade[1:])
    maxgap = 0
    for j in range(len(grade)-1):
        if maxgap < grade[j+1]-grade[j]:
            maxgap = grade[j+1]-grade[j]
    
    print(f"Class {i+1}")
    print("Max {}, Min {}, Largest gap {}".format(max(grade),min(grade),maxgap))