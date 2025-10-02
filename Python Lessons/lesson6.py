#strings

string_one = 'Hello'
string_two = "Hello"
string_three = '''Hello'''

print(string_one, string_two, string_three)

name = "Kevin"
age = 20

print("My name is {} and I am {} years old".format(name, age)) #".format method

print("My name is {name} and I am {age} years old".format(name="Kevin", age=20)) #".format method with keywords

print("I can use many times the same variable: {name}, {name}, {name}".format(name="Kevin")) #".format method with multiple uses of the same variable

var1 = "Kevin"

print("First letter of my name is: {}".format(var1[0])) #".format method with indexing

print("Last letter of my name is: {}".format(var1[-1])) #".format method with negative indexing

country = "Japan"

#print(country[6]) #IndexError: string index out of range

name_one = "Ben"
surname_one = "Ten"

full_name = name_one + " " + surname_one #string concatenation

print(full_name)

city = "New York"
#city[0] = "P"
#print(city) #TypeError: 'str' object does not support item assignment

var2 = "Hello World"
print(var2[1:]) #slicing from index 1 to the end
print(var2[:5]) #slicing from the beginning to index 5 (not included)
print(var2[1:5]) #slicing from index 1 to index 5 (not included)

item1 = "Good days to you!"

print(item1.lower()) #lowercase
print(item1.upper()) #uppercase

print(item1.split()) #split string into a list of words
print(item1.split("o")) #split string into a list using "o" as separator
