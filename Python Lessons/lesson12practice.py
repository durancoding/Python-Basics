#practice for previous lessons

print("I am practicing my python skills.")
print("And this is lesson 12!")
print("I am learning so much.")

name1 = "Mike"
surname1 = "Keller"
age1 = 18

print("Hello! My name is {name} {surname} and I am {age} years old.".format(name=name1, surname=surname1, age=age1))
print(f"Hey there! I'm {name1} {surname1} and I'm {age1} years old.")

GPA = 3.9

print(type(GPA))
if GPA > 2.5:
    pass_status = True
else:
    pass_status = False

print(pass_status)
if pass_status:
    print("You passed!")
else:
    print("You failed!")

GPA = int(GPA)
print(GPA)

coin = 0
monsters = 10
monster_drop_coin = 3

alive = True

if alive:        #basic game logic
    print("You are alive!")
    coin += monsters * monster_drop_coin
    print(f"You have {coin} coins.")
#basic calculator
"""""

first_number = (input("Enter first number: "))
second_number = (input("Enter second number: "))
operator = (input("Choose the operator 1=+, 2=- 3=* 4=/ 5=**: "))

if operator == "1":
    result = int(first_number) + int(second_number)
    print(f"{first_number} + {second_number} = {result}")
elif operator == "2":
    result = int(first_number) - int(second_number)
    print(f"{first_number} - {second_number} = {result}")
elif operator == "3":
    result = int(first_number) * int(second_number)
    print(f"{first_number} * {second_number} = {result}")
elif operator == "4":
    result = int(first_number) / int(second_number)
    print(f"{first_number} / {second_number} = {result}")
elif operator == "5":
    result = int(first_number) ** int(second_number)
    print(f"{first_number} ** {second_number} = {result}")
else:
    print("Invalid operator")

"""""

"""""

number1 = input("Enter a number: ") #check if number is even or odd
if int(number1) % 2 == 0:
    print(f"{number1} is even")
elif int(number1) % 2 != 0:
    print(f"{number1} is odd")
else:
    print("Invalid input")

"""""

#I <3 Python! and input function

"""""

user_name = input("Enter your name: ")
print(f"First letter of your name is: {user_name[0].upper()}")
print(f"Last letter of your name is: {user_name[-1].lower()}")

"""""

"""""

name_1 = input("Enter your name: ")
surname_1 = input("Enter your surname: ")

full_name_1 = name_1 + " " + surname_1

print(f"Welcome, {full_name_1}!")

full_name_1 = full_name_1.split(" ")
print(full_name_1)

"""""

"""""

number1 = input("Enter a number between 100 and 1000:")

if number1.isdigit() and 100 <= int(number1) <= 1000:
    digits = list(number1)
    print(digits)
else:
    print("Invalid input")

"""""

#simple captcha
"""""

my_list = [1,2,3,4,5]

authentication = input(f"What is the sum of these numbers? {my_list}: ")

if int(authentication) == sum(my_list):
    print("You are human!")
else:
    print("You are a robot!")

"""""


"""""

name2 = input("Enter your name: ")
surname2 = input("Enter your surname: ")
city = input("Enter your city: ")
dictionary1 = {'name': name2, 'surname': surname2, 'city': city}
print(dictionary1["name"])
print(dictionary1.values())

"""""

#tuples , sets and booleans

tuple1 = (1,2,3,4,5)
print("Tuple1:", tuple1)
print("First item of tuple1:", tuple1[0]) #indexing

set1 = {1,2,3,4,5}
print("Set1:", set1)
set1.add(6) #adding an element

if 3 in set1: #membership test
    print("3 is in set1")
else:
    print("3 is not in set1")

print("Boolean values:", True, False)
print("5 > 3:", 5 > 3) #comparison

#loops

#while loop

"""""
numb2 = 0

if numb2 < 5: 
    while numb2 < 5:
        print("Numb2 is:", numb2)
        numb2 += 1
else:
    print("Numb2 is not less than 5")

for i in range(1, 6):
    print("For loop iteration:", i)
else:
    print("For loop completed all iterations.")

"""""