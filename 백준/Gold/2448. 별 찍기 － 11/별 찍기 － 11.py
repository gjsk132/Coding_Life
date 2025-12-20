input = open(0).readline

lines = int(input())

shape = ["  *  ", " * * ","*****"]

def level_up(pre):

    now = len(pre)//3 * 2
    
    length = now*5+(now-1)
    side_gap = (length//2 + 1)//2

    next_shape = []

    for s in shape:
        next_shape.append(" "*side_gap+s+" "*side_gap)
    
    for s in shape:
        next_shape.append(s+" "+s)
    
    return next_shape

while not len(shape) == lines:
    shape = level_up(shape)

for i, s in enumerate(shape):
    if i == lines-1:
        print(s)
    else:
        print(s, end=" \n")