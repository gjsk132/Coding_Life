input = open(0).readline

def find_squares(size):
    square_cnt = 0

    for n in range(1, size+1):
        square_cnt += pow(size+1-n, 2)
    
    return square_cnt

while (size:=int(input())):
    print(find_squares(size))