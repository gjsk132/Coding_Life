input = open(0).readline

cnt = int(input())

target = "WOW"

for _ in range(cnt):
    string = input().strip()
    answer = 0

    for i in range(0, len(string)-2):
        if string[i:i+3] == target:
            answer += 1
    
    print(answer)