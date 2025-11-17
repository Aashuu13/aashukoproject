#age=str(22)
#print(type(age))class type


#fruits='mango'
#print(len(fruits)) length count


#password='aa11bb2233cc' condition
#if len(password)>8:
#    print('valid')
#else:
 #   print('invalid')


#grades={'ram':'a+','shyam':'a+'} #dictionary
#result=list(grades.values())
#step2=result.count('a+')
#print(step2)

#user_input='python python is good' #string (counts no of same word)
#result=user_input.count('python')
#print(result)

#replace method
#user_input= "i am spiderman"
#result=user_input.replace('spiderman','human')
#print(result)


#remove prefix method
#user_input= "i am spiderman"

#print(user_input.removeprefix('i'))

#new_input=user_input[:5]+"human"  slicing method
#print(new_input)

user_input='spiderman' #maketrans with tranlslate changes sinle letter
result=user_input.maketrans('s','S')
print(user_input.translate(result))



#print(ord('b')) #ascii value
#print('A'>'a') #compare ascii value



user_input='spiderman' #make trans convert to ascii value
result=user_input.maketrans('s','S')
print(result)

#to remove space
name='  laxmi  prasad  devkota  '
step1=name.strip()
step2='_'.join(step1.split())
print(step2)


#to make each words first letter capital AND REVRSE IT
user='i love south indian movies'
step1=user.title()
print(step1)
step2=user.split()
print((step1[::-1]))

email='laxman.kc123@gmail.com'
step1=email.split('@')[0]
step2=step1.replace('.','')
print(step2)





user_input= input("enter your email")
result=user_input.replace("@gmail.com"," ")      #ask user for email 
result=result.replace(".","")
print(result)