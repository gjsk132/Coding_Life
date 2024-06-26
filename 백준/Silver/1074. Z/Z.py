input = open(0).readline

n, row, col = map(int,input().split())

def z_setting(r, c, size):
    cnt = 0
    
    if size == 0:
        return 0

    ns = size//2

    if r <= row < r+ns and c <= col < c+ns:
        cnt += z_setting(r, c, ns)
    elif c <= col < c+ns:
        cnt += z_setting(r+ns, c, ns) + ns**2 * 2
    elif r <= row < r+ns:
        cnt += z_setting(r, c+ns, ns) + ns**2
    else:
        cnt += z_setting(r+ns, c+ns, ns) + ns**2 * 3
        
    return cnt

print(z_setting(0,0,2**n))