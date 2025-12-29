a=input("enter a url:")
domain=a.replace('http://','').replace('https://','').split('/')[0]
print("Domain:",domain)