a=eval(input('enter the cost price'))
if a>100000:
    b=a*0.15
    print('the tax to be paid is:',b)
elif a<50000 and a<=100000:
    b=a*0.10
    print('the tax to be paid is :',b)
elif a<=50000:
    b=a*0.05
    print('the tax to be paid is :',b)      
else:
    print('no tax')    