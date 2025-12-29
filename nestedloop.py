# #multiplication table using nested loops
# a=[4,5,6,7]
# for i in a:
#     for j in range(1,11):
#         print(f'{i}x{j}={i*j}')
#         print()

# #multiplication table of 4 and 6
# a=[4,5,6,7]
# for i in a:
#     for j in range(1,11):
#         if i==4 or j==6:
#             print(i,'x',j,'=',i*j)
#             print()
            
# #using count
# count=0
# for i in range[5,10,15]:
#     count+=1
#     print(count)

# #emails
# email=[1,2,3]
# for m in email:
#     print("new mail")
# print("done")

# #pattern
# for i in [1,2]:
#     print('a')
#     for j in [1]:
#         print('b')    

# #point
# points=[1,2,3]
# for p in points:
#     print(p*2) 
# #S           

for i in range(3):
    print("sent")

# folder
folders=['inbox','drafts','sent']
for sub in folders:
    print(f'sub folder:{sub}')
    for email in range(3):
        print(f'email {email+1} in {sub} folder')    

name='snap' 
for letter in name:
    print(letter)      


a=[3,5,7,13]
sum=0
c=2
for i in range(4):
    sum=sum+a[c]
    print(sum)      

b=[4,9,11,13]
sum=0
for i in range(4):
    for j in range(2):
        sum=sum+b[0]
        print(sum)