#qn1
Items = [3,5,7,9,11,13]
item = Items.pop(4)
Items.insert(1, item)
Items.append(item)
print(Items)
#=================================================================================================#
#qn2
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
intersection = first_set & second_set
first_set-= intersection
print(first_set)
#=================================================================================================#
#qn3
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
if first_set.issubset(second_set):
    first_set.clear()
elif first_set.issuperset(second_set):
    first_set.clear()
elif second_set.issubset(first_set):
    second_set.clear()
elif second_set.issuperset(first_set):
    second_set.clear()
print(first_set, second_set)
#================================================================================================#
#qn4
month = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
result = list(set(month.values()))
print(result)
#==================================================================================================#
#qn5
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique = list(set(sample_list))
t = tuple(unique)
print(t)
print(min(t), max(t))
#====================================================================================================#
#qn6
# if i > j and i > k:
#     print(i)
# elif j > i and j > k:
#     print(j)
# else:
#     print(k)
#=======================================================================================================#
#qn7
club_A = {"Alice", "Bob", "Charlie"}
club_B = {"David", "Eve", "Bob"}
if club_A & club_B:
    print("There is an overlap!")
else:
    print("No overlap between clubs.")
#======================================================================================================#
#qn8
# if i < j and j < k:
#     print("Ascending")
# elif i > j and j > k:
#     print("Descending")
# else:
#     print("Neither")
#====================================================================================================#
#qn9
student = {"name": "Ram", "course": "Math", "grade": 75}
valid_courses = {"Math", "Science", "English"}
min_grades = {"Math": 70, "Science": 65, "English": 60}
name = student["name"]
course = student["course"]
grade = student["grade"]
if course not in valid_courses:
    print("Invalid course.")
elif grade < min_grades[course]:
    print(f"Grade too low for {course}.")
else:
    print(f"{name} approved for {course}.")
#=====================================================================================================#
#qn10
required_tasks = {"Email", "Report", "Meeting"}
completed_tasks = {"Email", "Report"}
if required_tasks.issubset(completed_tasks):
    print("All tasks done!")
else:
    print("Some tasks pending.")
#====================================================================================================#
#qn11
contacts = {
    "Ram Bahadur": "ram@gmail.com",
    "Sita Kumari": "sita@gmail.com"
}
name = input("Enter name: ")
if name in contacts:
    print("Email:", contacts[name])
else:
    print("Contact not found.")
#======================================================================================================#
#qn12
shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}
remaining = shopping_list - bought
if remaining:
    print(f"Still need to buy: {remaining}")
else:
    print("Shopping complete!")
#=======================================================================================================#
#qn13
class_list = ["ram", "sita", "laxman"]
new_student = "ram"
if new_student in class_list:
    print("ram is already in class.")
else:
    class_list.append(new_student)
    print("Added ram.")
#======================================================================================================#
#qn14
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
count = votes.count("Blue")
if count >= 3:
    print("Blue wins!")
else:
    print("Blue did not win.")
#====================================================================================================#
#qn15
grades = {"Ram": 92, "Sita": 88}
student = "Laxman"
if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"Grade not available for {student}.")
#=====================================================================================================#
#qn16
student = {"name": "Ram", "course": "Robotics", "grade": 9}
valid_courses = {"Creative Writing", "Robotics", "Digital Art"}
name = student["name"]
course = student["course"]
grade = student["grade"]
if course not in valid_courses:
    print(f"{name} selected an invalid course.")
elif grade < 9:
    print(f"{name} is not eligible for {course} (grade too low).")
elif course == "Robotics" and grade == 9:
    print(f"{name} is not eligible for Robotics (grade too low).")
else:
    print(f"{name} is approved for {course}.")
#========================================================================================================#
#qn17
applicant = {
 "name": "Priya",
 "skills": ["Java", "SQL"],
 "experience_years": 1
}
required_skills = {"Python", "Java"}
if set(applicant["skills"]) & required_skills and applicant["experience_years"] >= 2:
    print("Priya qualifies.")
else:
    print("Priya does not qualify.")
#============================================================================================================#
#qn18
banned_items = {"scissors", "knife", "lighter"}
weight = float(input("Enter baggage weight: "))
item = input("Enter item: ").lower()
if weight <= 7 and item not in banned_items:
    print("Bag accepted.")
else:
    print("Bag not allowed.")
#=============================================================================================================#
#qn19
group1 = {"A", "B", "C"}
group2 = {"D", "E", "C"}
if group1 & group2:
    print("Warning: Groups share at least one student!")
else:
    print("Groups are OK – no overlap.")
#=============================================================================================================#
#qn20
salary = {"ram": 5000, "shyam": 6000, "hari": 7000}
salary["shyam"] = 8500
print(salary)
#==============================================================================================================#
#qn21
riya = {"bread", "butter", "jam", "tea"}
anjali = {"butter", "jam", "coffee", "eggs"}
result = riya - anjali
if result:
    print(f"Riya has extra items: {result}")
else:
    print("Riya has no extra items.")
#==============================================================================================================#
#qn22
alice_items = {"pen", "notebook"}
bob_items = {"bag", "lunch"}
if alice_items.isdisjoint(bob_items):
    print("They picked completely different items.")
else:
    print("They have some common items.")    
#===================================================================================================================#




# MCQ answers
# Q1 Answer
# b) Removes and returns the item with the specified key
# Q2 Answer
# d) None of the above (direct assignment is used: dict[key] = value)
# Q3 Answer
# b) 2
# 4
# Q4 Answer
# a) keys()
# Q5 Answer
# a) items()
# Q6 Answer
# b) 2
# Q7 Answer
# c) in operator
# Q8 Answer

# a) True
   
    
   

