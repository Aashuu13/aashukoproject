#a=input('enter a string:')
#b=a.lower().title.split()        
#print(''.join(b))




#password=input('enter a string:')
#step1=len(password)-2
#step2=password[0]+'*'*step1+password[-1]
#print(step2)




a=input("enter a url:")
b=a.replace('http://www.','').replace('https://www.','').replace('http://','').replace('https://','')
c=b.split('.')
print(c[0])