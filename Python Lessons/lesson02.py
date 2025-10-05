#Variables and Data Types
#This program demonstrates the use of variables and different data types in Python.

first_name = "John"  # String variable
last_name = "Doe"    # String variable

print("First Name:", first_name)

print(f"Last Name: {last_name}") # Using f-string for formatted output

age = 23 # Integer variable

print("His name is", first_name, last_name, "and he is", age, "years old.") # "Using commas to separate values in print

height = 5.9 # Float variable

print("He is", height, "feet tall.") # Printing float variable

# Boolean variable
is_student = True
print("Is he a student?", is_student) # Printing boolean variable

is_teacher = False
print("Is he a teacher?", is_teacher) # Printing boolean variable

print(f"{first_name} {last_name} is {age} years old, {height} feet tall, and it is {is_student} that he is a student.") # Using f-string for formatted output

if is_student:
    print(f"{first_name} is a student.")
elif is_teacher:
    print(f"{first_name} is a teacher.")
else:
    print(f"{first_name} is neither a student nor a teacher.") # This script demonstrates the use of variables and different data types in Python.

number_of_courses = 5 # Integer variable

is_student = False # Changing boolean variable
is_teacher = True # Changing boolean variable

if is_student:
    print(f"{first_name} is enrolled in {number_of_courses} courses.") # Printing integer variable
elif is_teacher:
    print(f"{first_name} teaches {number_of_courses} courses.") # Printing integer variable
else:
    print(f"{first_name} is neither a student nor a teacher.")