sh, sm, ss = map(int, input().split(':'))
eh, em, es = map(int, input().split(':'))

left_second = (eh*3600 + em*60 + es) - (sh*3600 + sm*60 + ss)

if left_second < 0:
    left_second += 24*3600

print(f'{left_second//(3600):02d}:{(left_second%3600)//60:02d}:{left_second%60:02d}')