items=[1,2,3,4,5,6,7,8,'a','b',-20,-28]
total=0
for i in items:
    if type(i)==int:
       if i>0:
           if i%2==0:
               total=total+i
print(total)                
# odd=[]
# even=[]
# letters=[]
# for i in items:
#  if type(i)==int:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#  else:
#         letters.append(i)
# print(odd)
# print(even)
# print(letters)
# items=[1,2,3,4,5,6,7,8,'a','b',-20,-28,]
# str='programming'
# # for i in str:
# #     if i in 'aeiou':
# #         print(f'{i} is vowel')
# #     else:
# #         print(f'{i} is consonant')
# consonant=set()
# vowel=set()
# for i in str:
#     if i in 'aeiou':
#         vowel.add(i)
#     else:
#         consonant.add(i)
# print(vowel)
# print(consonant)        
# grocery_items=["apple","milk","bread","eggs"]
# for i in range(len(grocery_items)):
#     if i+1==grocery_items:
#      print(grocery_items[i])
a=11
for i in range(1,11):
    b=a*i
    print(b)