input = open(0).readline

N, M, price = map(int, input().split())

plus = M*price
sale = ((M+1)*(100-N)*price)//100

answer = min(plus, sale)

print(answer)