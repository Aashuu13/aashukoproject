#data='ram'
#for i in data:
   # print(data)
   # print(i)
    #print(i,end='')
# items=[1,2,3,4,5]    
# # for i in items:
# #     if i%2==0:
# #        print('even numbers are:')
       

# if items[0]%2==0:
#     print(items[0])
# if items[0]%2==0:
#     print(items[1])
# if items[1]%2==0:
#     print(items[1])
# if items[2]%2==0:
#     print(items[2])            
# if items[3]%2==0:
#     print(items[3])    
# if items[4]%2==0:
#     print(items[4])    
items=[1,2,3,4,5,6,7,8,'a','b']
odd=[]
even=[]
letters=[]
for i in items:
    if i%2==0:
        even.append(i)
    elif isinstance(i, str):
        letters.append(i)
    else:
        odd.append(i)
print(odd)
print(even)
print(letters)