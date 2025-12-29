is_card_valid=True
balance=3000
pin=int(input('enter a valid pin'))
if is_card_valid: #empty and big bracket is false
    print('valid card')
    if pin==1234:
      print('valid pin')    
    else:
     print('invalid pin')
else:
    print('invalid card')
#-------------------------------------------------------------------------------------------------------------------
#a=int(input('enter a num:'))
#if a>0:
    #print('positive')
#elif a<0:
    #print("negative")
#else:
    #print('zero')
                       
a=int(input('enter a num:'))
if a>0:
    if a%2==0:
        print('even')
    else:
        print('odd')
elif a<0:
    print("negative")
else:
    print('zero')
 #if elif and else ko biccha ma statement aayo vane error aauxa
                                         