#conditional statement (control flow)
for i in range(5):
    print(i)
for i in range(5):
    if i==3:
        break
    print(i)    
for i in range(5):
    if i==3:
        continue
    print(i)  
def login():
    return 'good day'
    print('hello py')
print(login())          
#if elif else
age=11
if age > 18:
    print('can vote')

num1=11
num2=12
if num1==num2:
    print('equal')
elif num1>num2:
    print('num1 is greater')
else:
    print('num2 is greater')    
    
    