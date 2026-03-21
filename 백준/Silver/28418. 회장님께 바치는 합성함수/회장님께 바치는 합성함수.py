f = list(map(int, input().split()))
g = [0]+list(map(int, input().split()))

p, q = [0,0,0], [0,0,0]

p[0] = f[0]*g[1]**2
p[1] = f[0]*2*g[1]*g[2] + f[1]*g[1]
p[2] = f[0]*g[2]**2 + f[1]*g[2] + f[2]

q[0] = g[1]*f[0]
q[1] = g[1]*f[1]
q[2] = g[1]*f[2] + g[2]

p_q = [p[i]-q[i] for i in range(3)]

tmp = p_q[1]**2 - 4*p_q[0]*p_q[2]

if p == q:
    print("Nice")
elif not p_q[0] and not p_q[1] or tmp < 0:
    print("Head on")
elif tmp == 0 or not p_q[0]:
    print("Remember my character")
else:
    print("Go ahead")