def solution(numbers):
    answer = []
    
    # 각 number의 가능 여부를 추가
    for i in numbers:
        answer.append(int(checkTree(changeBin(i))))
    return answer

# 2진수로 바꿔주는 코드
def changeBin(num):
    num_str =  str(format(num, 'b'))
    i = 1
    while (i:= i*2):
        if len(num_str) < i : break
    
    return '0'*(i-len(num_str)-1)+num_str
    
# True False
def checkTree(num):
    if len(num) == 1:
        return True
        
    if num[len(num)//2] == '0' and ('1' in num):
        return False
    
    return (checkTree(num[:len(num)//2]) and checkTree(num[len(num)//2+1:]))
    