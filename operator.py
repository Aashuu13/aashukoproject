#arithmetic ops
num1=5
num2=3
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1//num2)
print(num1**num2)



#assignment ops
num1=10
num2=2
num1+=num2
print(num1)


items=[1,2,3,4]
items2=items
items+=items2
print(items)
print(items2)




items=[1,2,3,4]
items2=items
items=items+items2
print(items)
print(items2)


print([1,2,3,4]+[1,2,3,4])



# creating empty sets
a=set()
print(type(a))

a={*()}
print(type(a))



#comparision ops
num1=12
num2=13
print(num1==num2)
if num1==num2:
    print('equal')
else:
    print('not equal')
    
if num1>num2:
    print('1 is big')
else:
    print('2 is big')

if num1<num2:
    print('1 is small')
else:
    print('2 is small')
if num1!=num2:
    print('true')
else:
    print('false')



#logical ops
#(and,or,not)

#membership ops
stud=['harry','john','james']
inp=input('enter name:')
print(inp in stud)
if inp in stud:
    print(f'{inp}present')
else:
    print(f'{inp}absent')
#.....................................................................
if inp not in stud:
    print('true')
else:
    print('false')
    
#identity ops
name='hello'
name2='world'
print(id(name))
print(id(name2))
print(name is name2)


#bitwise ops
a=67
b=89
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)








