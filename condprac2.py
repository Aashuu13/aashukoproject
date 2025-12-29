a=int(input('enter a number:'))
if a%3==0 and a%5==0:
    print('fizzbuzz')
elif a%3==0 and a%5!=0:
    print('fizz')
elif a%5==0 and a%3!=0:
    print('buzz')
else:
    print(a)    
#-----------------------------------------------------------------------------------------------    
import random
result=random.randint(0,5)
if result==0:
    print('aashu turn evolved from eating atharva')
elif result==1:
    print('atharva is spoiled kid')
elif result==2:
    print('atharva cannot swim')
elif result==3:
    print('atharva is good dancer')
elif result==4:
    print('atharva is a monkey')
elif result==5:
    print('atharva is bad singer')                    
else:
    print('error')    