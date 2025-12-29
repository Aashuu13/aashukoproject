num1=int(input('enter first num:'))
num2=int(input('enter second num:'))
c=input('enter the operation:')
calc=0
if c=='+':
    calc=num1+num2
    print(calc)
elif c=="-":
    calc=num1-num2
    print(calc)    
elif c=="*":
    calc=num1*num2
    print(calc)
elif c=="/":
    calc=num1/num2
    print(calc)    
else:
    print("invalid")        