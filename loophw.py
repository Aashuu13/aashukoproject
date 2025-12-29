# Q1) Check even or odd from 1 to 5
for i in range(1, 6):
    print(f"{i} is {'Even' if i % 2 == 0 else 'Odd'}")

# Q2) Sum of elements in a list
lst = [10, 20, 30, 40]
print("Total Sum:", sum(lst))

# Q3) Personalized message for students
students = ["Ram", "Hari", "Sita"]
for name in students:
    print(f"Hi {name}, your course approval is ready!")

# Q4) Chapter page summary
pages = [45, 30, 50, 40]
for i, p in enumerate(pages, start=1):
    print(f"Chapter {i} has {p} pages.")

# Q5) Product of list elements
lst = [4, 5, 3, 2]
product = 1
for i in lst:
    product *= i
print(product)

# Q6) Multiplication table of 11
num = 11
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# Q7) Student approval status
students = [
    {"name": "ram", "math_grade": 43},
    {"name": "hari", "math_grade": 65},
    {"name": "sita", "math_grade": 90}
]
for s in students:
    s["status"] = "Approved" if s["math_grade"] >= 70 else "Rejected"
print(students)

# Q8) Common elements in two lists
a = [1,2,3,4,5]
b = [3,4,5,6,7]
for i in a:
    if i in b:
        print(i)

# Q9) Print 1 and 4 only
lst = [1,2,3,4]
for i in lst:
    if i in (1,4):
        print(i)

# Q10) Print 1, 2 and 4 only
lst = [1,2,3,4]
for i in lst:
    if i != 3:
        print(i)

# Q11) Replace 3 with "a"
lst = [1,2,3,4]
new = ["a" if i == 3 else i for i in lst]
print(new)

# Q12) Separate odd and even
lst = [1,2,3,4,5]
odd = [i for i in lst if i % 2 != 0]
even = [i for i in lst if i % 2 == 0]
print(odd)
print(even)

# Q13) Prime number check
num = 7
if num > 1 and all(num % i != 0 for i in range(2, num)):
    print("Prime")
else:
    print("Not Prime")

# Q14) Separate datatypes
lst = [1,2,3,4,"a","b"]
nums = [i for i in lst if isinstance(i, int)]
chars = [i for i in lst if isinstance(i, str)]
print(nums)
print(chars)

# Q15) Count letters and digits
s = "abc123"
letters = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)
print(letters, digits)

# Q16) Username and password validation
username = "admin"
password = "1234"
print("Valid" if username == "admin" and password == "1234" else "Invalid")

# Q17) Odd or even number
num = 8
print("Even" if num % 2 == 0 else "Odd")

# Q18) Factorial
num = 5
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)

# Q19) Multiplication tables 1 to 8
for i in range(1, 9):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()

# Q20) Print 1 and 2 only
lst = [1,2,3,4]
for i in lst:
    if i < 3:
        print(i)

# Q21) Sum of odd numbers
print(sum(i for i in range(1, 11) if i % 2 != 0))

# Q22) Sum of even numbers
print(sum(i for i in range(1, 11) if i % 2 == 0))

# Q23) Count spaces
s = "hello world python"
print(s.count(" "))

# Q24) Cube of elements
lst = [1,2,3,4]
print([i**3 for i in lst])

# Q25) Reverse a string
s = "programming"
print(s[::-1])

# Q26) Break at 8
for i in range(50):
    if i == 8:
        break
    print(i)

# Q27) Print every letter
for c in "hello":
    print(c)

# Q28) Hello with names only
a = ["ram","shyam",1,2]
for i in a:
    if isinstance(i, str):
        print("Hello!", i)

# Q29) Append Dr. prefix
a = ["ram","shyam",1,2]
print(["Dr." + str(i) for i in a])

# Q30) Square of each number
lst = [1,2,3,4]
print([i*i for i in lst])

# Q31) Positive numbers
lst1 = [111, 32,-9,-45,-17, 9, 85,-10]
print([i for i in lst1 if i > 0])

# Q32) Except 3 and 6
lst = [0,1,2,3,4,5,6]
for i in lst:
    if i not in (3,6):
        print(i)

# Q33) Append type of each element
lst = [1,"a",2.5]
print([type(i) for i in lst])

# Q34) For loop with else
for i in range(5):
    print(i)
else:
    print("Done")

# Q35) Series 105 to 7
for i in range(105, 0, -7):
    print(i)

# Q36) Remove bad characters
bad_chars = [';', ':', '!', '*']
s = "py;th* o:n ! ;py * t*h:o !n"
print("".join(c for c in s if c not in bad_chars and c != " "))

# Q37) Count even and odd
lst = [1,2,3,4,5]
even = sum(1 for i in lst if i % 2 == 0)
odd = sum(1 for i in lst if i % 2 != 0)
print(even, odd)

# Q38) Sum of multiples of 3 or 5
print(sum(i for i in range(100) if i % 3 == 0 or i % 5 == 0))

# Q39) Sum of even and odd separately
even = sum(i for i in range(1, 101) if i % 2 == 0)
odd = sum(i for i in range(1, 101) if i % 2 != 0)
print(even, odd)

# Q40) Palindrome number
num = 121
print("Palindrome" if str(num) == str(num)[::-1] else "Not Palindrome")

# Q41) Armstrong number
num = 153
digits = str(num)
total = sum(int(d)**len(digits) for d in digits)
print("Armstrong" if total == num else "Not Armstrong")

# Q42) Remove vowels from string
s = "programming"
print("".join(c for c in s if c not in "aeiou"))
