h, m = map(int, open(0).readline().split())
total = (h*60+m-45)%1440
print(total//60, total%60)