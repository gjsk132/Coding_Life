input = open(0).readline

num_eight = "0o"+input().strip()

print(bin(int(num_eight, 8))[2:])