input = open(0).readline

def count_carry(n1, n2):
    total_carry, now_carry = 0, 0

    while n1 or n2:
        now_carry = (n1%10 + n2%10 + now_carry) // 10
        total_carry += now_carry
        n1, n2 = n1//10, n2//10

    return total_carry

while True:
    num1, num2 = map(int, input().split())

    if not num1 and not num2:
        break
    
    print(count_carry(num1, num2))