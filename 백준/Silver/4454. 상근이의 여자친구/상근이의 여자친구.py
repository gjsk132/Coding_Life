input = open(0).readline

def binary_search(start, end, cnt=0):

    if int(start*100) == int(end*100):
        return str(start)

    mid = (start + end)/2

    total_oil = ((a*mid**3 + b*mid**2 + c*mid + d) * m)

    if total_oil <= t:
        start = mid
    else:
        end = mid

    return binary_search(start, end, cnt+1)

while (string := input()):
    try:
        a, b, c, d, m, t = map(float, string.split())
        num, decimal = map(str, binary_search(0, 1000).split('.'))
        print("{}.{}".format(num, decimal[:2]))
    except EOFError:
        break