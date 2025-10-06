#practices with ChatGPT
#level 1 "Warm Up"

"1 -" "What is the difference between '==' and is in Python?"

# '==' checks for value equality, while 'is' checks for identity (same object in memory).

example_list1 = [1, 2, 3]
example_list2 = [1, 2, 3]
print(example_list1 == example_list2)  # True, because values are the same
print(example_list1 is example_list2)  # False, because they are different objects in memory

"2 -" "What will this print?: print('Hello' * 3)"

print('Hello' * 3)  # This will print 'HelloHelloHello'

"3 -" "Convert this list to a set and explain what happens: lst = [1, 2, 2, 3, 4, 4]"

lst = [1, 2, 2, 3, 4, 4]
lst = set(lst)

print(lst) #the same elements in the lists are gone

"4 - " "Write one line of code to get the last element of this list:"

fruits = ["apple", "banana", "cherry"]

print(fruits[-1])

"5 - " "Create a dictionary called student with keys 'name','age', and 'grades', then print the student's name."

students = {"name": "Ben", "age": 20, "grades" : 100}

print(students["name"])

# Level 2: Logic & Problem Solving
"6 - " "Write a function that takes a list of numbers and returns a new list containing only the even numbers."

list1 = list(range(1,10))
"""
for num in list1:
    if num %2 == 0:
        pass
    else:
        list1.remove(num)

print(list1)

or

def get_even_numbers(numbers):
    return [num for num in numbers if num %2 == 0] 

print(get_even_numbers(list(range(1, 10))))
"""

"7 - " "Using a lambda expression, return the square of each number in the list [1, 2, 3, 4, 5]."

list2 = [1, 2, 3, 4, 5]

square = lambda x: x**2

for i in list2:
    print(square(i))

"8 - " "Write a loop that prints numbers from 10 down to 1 (inclusive)."

for i in range(10, 0 ,-1):
    print(i)

"9 - """"Use a for loop to print each person's name and age in the format:"""

people = {"Alice": 25, "Bob": 30, "Charlie": 20}

names = list(people.keys())
ages = list(people.values())

num2 = 0
for i in range(3):
    print(f"{names[num2]} is {ages[num2]} years old")
    num2 += 1

"10 - " "Explain what this code prints and why:"

a = [1, 2, 3]
b = a
b.append(4)
print(a)

#because we can add new elements in a list

#Level 3: Mini Project Challenge

"11 - "
"""
Write a function word_count(text) that:

Takes a string (sentence)

Returns a dictionary showing how many times each word appears
"""

def word_count(text):
    words = text.split()
    dictionary1 = {}
    for word in words:
        if word in dictionary1:
            dictionary1[word] += 1
        else:
            dictionary1[word] = 1
    return dictionary1

print(word_count(input("Please enter a sentence: ")))