input = open(0).readline
n = int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_list.sort()
b_list.sort(reverse = True)
result = 0
for i, j in zip(a_list, b_list):
    result += i*j
    
print(result)