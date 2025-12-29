items={'1.':{'question':'which symbol is used to comment in python',
             'options':{'a':'/','b':'#','c':'//','d':'*/*'},'correct_answer':'b'},
       '2.':{'question':'which method is used to add a element in list',
             'options':{'a':'append()','b':'add()','c':'addlist()','d':'update()'},'correct_answer':'a'}}
score=0
for i,j  in items.items():
    print(i,'',j['question'])
    for key,value in j['options'].items():
        print(key,'',value)
    guess=input('choose the correct options:(a,b,c,d)')
    if guess==j['correct_answer']:
        score+=1

print(f'final score is:{score}')
