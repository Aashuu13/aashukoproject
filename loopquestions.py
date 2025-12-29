# str=input("Enter the Desired String = ")
# vowel=[]
# for i in str:
#     if i in 'aeiou' and i not in vowel:
#         vowel.append(i)
# print(vowel)

dictionary={}
user_input=int(input('how many words do you want to add:'))
for i in range(1,user_input+1):
    choice=input('press 1. add 2. display 3. remove 4. exit:')
    if choice==1:
        word=input('Enter a word: ')
        if word in dictionary:
            print(f'{word} already exists')
        else:
            meaning=input('enter a meaning of given word: ')
            dictionary[word]=meaning
    elif choice==2:
        for i,j in dictionary.items():
            print(i,'',j)
    elif choice==3:
        word=input('enter a word you want to remove: ')
        if word not in dictionary:
            print(f'{word} not found')
        else:
            dictionary.pop(word)
    elif choice==4:
        break        