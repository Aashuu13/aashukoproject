# check odd even
a=int(input('enter a number:'))
if a%2==0:
    print('even')
else:
    print('odd')
#------------------------------------------------------------------------------------------------------------#
#check vowel or consonant
ch=(input('enter a character:'))
if ch==("a" ) :
    print('vowel')
elif ch==('e'):
    print('vowel')
elif ch==('i'):
    print('vowel')
elif ch==('o'):
    print('vowel')
elif ch==('u'):
    print('vowel')   
             
else:
    print('consonant')        
#------------------------------------------------------------------------------------------------------------#
#check adult or minor
b=int(input('enter the age:'))
if b>=18:
    print('atharva is adult')
elif b<18:
    print('atharva is a minor')    
#--------------------------------------------------------------------------------------------------------------#
#check pass or fail
c=int(input('enter the marks:'))
if c>=40 and c<=100:
    print('pass')
else:
    print('fail')   
#--------------------------------------------------------------------------------------------------------------#
#check largest among 3  
w=int(input("enter first number:"))
x=int(input('enter second number:'))
y=int(input('enter third number:'))
if w>x and w>y:
    print('w is largest')
else:
    if x>y:
        print('x is largest')
    else:
        print('y is largest')  
#------------------------------------------------------------------------------------------------------------#
#check month name 
m=int(input('enter the month '))  
if m==1:
    print('january')
elif m==2:
    print('february')
elif m==3:
    print('march') 
elif m==4:
    print('april')
elif m==5:
    print('may')
elif m==6:
    print('june')
elif m==7:
    print('july')
elif m==8:
    print('august')
elif m==9:
    print('september')
elif m==10:
    print('october')   
elif m==11:
    print('november')
elif m==12:
    print('december')
else:
    print("invalid")
#----------------------------------------------------------------------------------------------------------------#
#check hot or cold
temp=int(input('enter the temperature')) 
if temp>35:
    print('hot')
elif temp>=25 and temp<35:
    print('warm') 
elif temp<25:
    print('cold') 
#----------------------------------------------------------------------------------------------------------------#
#check salary
s=int(input('enter the salary'))
if s>50000:
    print('high salary')
elif s>=30000 and s<50000:
    print('medium salary')
elif s<30000:
    print('low salary')       
#-----------------------------------------------------------------------------------------------------------------#
#check positive negative zerp
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
#-----------------------------------------------------------------------------------------------------------------#
#check weekday or weekend
day = int(input("Enter day number (1-7): "))

if day == 6 or day == 7:
    print("Weekend")
else:
    print("Weekday")
#-----------------------------------------------------------------------------------------------------------------#
#check divisible by 5 and 7
numm = int(input("Enter a number: "))

if numm % 5 == 0 and numm % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible by both 5 and 7")
#-------------------------------------------------------------------------------------------------------------# 
#positibe negative zero
num = int(input("Enter a number: "))
if num > 0:
     print("Positive")
elif num < 0:
     print("Negative")
else:
     print("Zero")
#----------------------------------------------------------------------------------------------------------------#
#check num btwn 1 and 100
num=int(input('Enter a number: '))
if num>0 and num<101:
    print('Number is between 1 and 100')
else:
     print('Number is not between 1 and 100')
#----------------------------------------------------------------------------------------------------------------#     
#check even odd
number=int(input('Enter a number :'))
if number%2==0:
    print('number is even')
elif number%2!=0:
    print('number is odd')
else:
    print('error')
#----------------------------------------------------------------------------------------------------------------#
#check grades
grade=int(input('What is your marks(Q4):'))
if 89<grade<100:
    print('Your grade is A+')
elif 79<grade<90:
    print('Your grade is A')
elif 69<grade<80:
    print('Your grade is B+')
elif 59<grade<70:
    print('Your grade is B')
elif 49<grade<60:
    print('Your grade is C')
elif 39<grade<50:
    print('Your grade is D')
else:
    print('Your grade is E')

#----------------------------------------------------------------------------------------------------------------#
#calculator
num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))
calc=input('What do you want to do, addition, multiplication, substraction, or division:')

if calc=='addition':
    result=(num1+num2)
    print(f'addition result is {result}')
elif calc=='multiplication':
    result=(num1*num2)
    print(f'your result is {result}')
elif calc=='substraction':
    result=(num1-num2)
    print(f'your result is {result}')
elif calc=='division':
    result=(num1/num2)
    print(f'Your result is {result}')
else:
    print('invalid')
#-----------------------------------------------------------------------------------------------------------------#
#check voting age
age=int(input('Enter your age:'))
if age<18:
    print('you r eligible to vote')
else:
    print('you are not eligible')
#------------------------------------------------------------------------------------------------------------------#
#login system
usn=(input('(Q7)Enter your username:'))
username='aashu'
password='aashu123'
if usn==username:
    print('valid username')
    psw=(input('Enter a password:'))
    if psw==password:
        print('you have logged in')
    else:
        print('wrong password')
else:
    print('invalid username')
#-----------------------------------------------------------------------------------------------------------------#
#check divisible by 7
num=int(input('Enter a number:'))
if num%7==0:
    print('the number is divisible by 7')
else:
    print('Number is not divisible by 7')
#-------------------------------------------------------------------------------------------------------------------#
#check votinga age
age=int(input('Enter your age:'))
if age<18:
    print('you r eligible to vote')
else:
    print('you are not eligible')
#------------------------------------------------------------------------------------------------------------------#
#check equal numbers
num1=int(input('Enter first number:'))
num2=int(input('Enter second number:'))
num3=int(input('Enter third number:'))
if num1==num2 and num2==num3:
    print('All numbers are equal')
elif num1==num2 and num1!=num3:
    print('2 numbers are equal')
elif num2==num3 and num2!=num1:
    print('2 numbers are equal')
elif num1==num3 and num1!=num2:
    print('2 numbers are equal')
else:
    print('All numbers are different')  
#----------------------------------------------------------------------------------------------------------------#  
#divisible by 7 or not
nummm = int(input("Enter a number: "))

if nummm % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is NOT divisible by 7.")
#-----------------------------------------------------------------------------------------------------------------#
 #fizzbuzz
a=int(input('enter a number:'))
if a%3==0 and a%5==0:
    print('fizzbuzz')
elif a%3==0 and a%5!=0:
    print('fizz')
elif a%5==0 and a%3!=0:
    print('buzz')
else:
    print(a)  
#============================================================================================================#
#checking
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
    
    if num % 2 == 0:
        print("It is even.")
    else:
        print("It is odd.")
else:
    print("The number is not positive.")
#----------------------------------------------------------------------------------------------------------#
#lift 
current_floor = 5
pressed_floor = int(input("Enter the floor number you pressed: "))

if pressed_floor > current_floor:
    print("The lift should go UP.")
elif pressed_floor < current_floor:
    print("The lift should go DOWN.")
else:
    print("The lift should STAY at the current floor.")
#---------------------------------------------------------------------------------------------------------#
#positive negative zero and equal
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("The greater number is:", num1)
else:
    if num2 > num1:
        print("The greater number is:", num2)
    else:
        print("Both numbers are equal.")

        if num1 > 0:
            print("The number is positive.")
        else:
            if num1 < 0:
                print("The number is negative.")
            else:
                print("The number is zero.")
#--------------------------------------------------------------------------------------------------------#
#importing 
import random

num = random.randint(0, 5)

print("Random number:", num)

if num == 0:
    print("Flamingos turn pink from eating shrimp.")
elif num == 1:
    print("The only food that doesn't spoil is honey.")
elif num == 2:
    print("Shrimp can only swim backwards.")
elif num == 3:
    print("A taste bud's life span is about 10 days.")
elif num == 4:
    print("It is impossible to sneeze while sleeping.")
else:
    print("It is illegal to sing off-key in North Carolina.")
#---------------------------------------------------------------------------------------------------------#
#marks in 4 subjects
# Accept marks of four subjects
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
total = m1 + m2 + m3 + m4
percentage = total / 4
print("Total Marks:", total)
print("Percentage:", percentage)
if percentage > 70:
    print("Grade: Distinction")
elif percentage > 60:
    print("Grade: First Division")
elif percentage > 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")
#--------------------------------------------------------------------------------------------------------#
#road tax 
a=eval(input('enter the cost price'))
if a>100000:
    b=a*0.15
    print('the tax to be paid is:',b)
elif a<50000 and a<=100000:
    b=a*0.10
    print('the tax to be paid is :',b)
elif a<=50000:
    b=a*0.05
    print('the tax to be paid is :',b)      
else:
    print('no tax')  
#-------------------------------------------------------------------------------------------------------#
# Accept salary and years of service
salary = float(input("Enter your salary: "))
years = float(input("Enter years of service: "))
if years > 10:
    bonus = salary * 0.10
    print("Bonus =", bonus)
elif years >= 6 and years <= 10:
    bonus = salary * 0.08
    print("Bonus =", bonus)
else:
    bonus = salary * 0.05
    print("Bonus =", bonus)       
#------------------------------------------------------------------------------------------------------#
#score evaluation
score = float(input("Enter subject score: "))
if score > 90:
    print("Congratulations!")
elif score >= 50 and score <= 90:
    print("Good, but you should improve.")
else:
    print("You should consider retaking the course.")        
#------------------------------------------------------------------------------------------------------------#
#job eligibility
age = int(input("Enter age: "))
if age >= 18:
    degree = input("Do you have a degree? (yes/no): ").lower()

    if degree == "yes":
        experience = float(input("Enter years of work experience: "))

        if experience > 3:
            print("Highly Eligible.")
        elif experience >= 1:
            print("Eligible.")
        else:
            print("Under Review.")
    else:
        print("Not eligible (degree required).")
else:
    print("Not eligible (age below 18).")     
#-----------------------------------------------------------------------------------------------------------#
#wage based on age,gender and days
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of working days: "))
if age >= 18 and age < 30:
    if gender == "M":
        wage_per_day = 700
    else:
        wage_per_day = 750

elif age >= 30 and age <= 40:
    if gender == "M":
        wage_per_day = 800
    else:
        wage_per_day = 850
else:
    wage_per_day = 0
    print("Age does not fall in wage categories.")
if wage_per_day > 0:
    total_wage = wage_per_day * days
    print("Total Wage:", total_wage)
#--------------------------------------------------------------------------------------------------------------#
#atm simulation
is_valid = True
balance = 50000
correct_pin = 123
if is_valid:
    pin = int(input("Enter your PIN: "))
    if pin == correct_pin:
        print("\n--- ATM Menu ---")
        print("1. Withdraw")
        print("2. Check Balance")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance.")
        else:
            if choice == 2:
                print("Your current balance is:", balance)
            else:
                if choice == 3:
                    print("Thank you for visiting!")
                else:
                    print("Invalid option.")
    else:
        print("Incorrect PIN.")
else:
    print("Card is not valid.")
#---------------------------------------------------------------------------------------------------------------#
   
                                                             