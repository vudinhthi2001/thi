a=int(input('nhap a: '))
b=int(input('nhap b: '))
c=int(input('nhap c: '))
i=b*b - 4*a*c
if i>0:
    x1=(-b+sprt(i))/2*a
    print(x1)
    x2=(-b-sprt(i))/2*a
    print(x2)
elif i==0:
    x=-b/2*a
    print(x)
else:
    print('vo nghiem')
    
