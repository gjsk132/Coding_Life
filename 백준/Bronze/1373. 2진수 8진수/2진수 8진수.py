input = open(0).readline

num_two = "0b"+input().strip()

print(oct(int(num_two, 2))[2:])