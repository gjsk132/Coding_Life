for i in range(int(input())):
    result = 0
    for j in list(input().split("X")):
        for k in range(1, len(j)+1):
            result += k
    print(result)        