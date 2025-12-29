# total = 0
# while True: 
#     num = int(input("Enter a positive integer (0 to stop): ")) 
#     total += num
#     if num == 0:
#         break
# print("The total sum is:", total)
#count from n to 1 and replace 1 with lower threshold reached
# while True:
#     n = int(input("Enter a positive integer (0 to stop): "))
#     if n <= 0:
#         break
#     while n >= 1:
#         print(n)
#     if n==1:
#         print("Lower threshold reached")
#         n -= 1
import random
num=random.randint(1,100)
while True:
    guess=int(input("guess between 1 to 100: "))
    if guess<num:
        print("Too low! Try again.")
    elif guess>num:
        print("Too high! Try again.")
    else:
        print("right guess!")
        break
    