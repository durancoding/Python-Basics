#basic algorithms and numbers

print("Divison:" , 10 / 2) # Division

print("Power of number:", 2 ** 5) # Exponentiation

print("Result is: " , 10 + 3 * 5 - 8 / 2) # Mixed operations

number = 15
if number % 2 == 0:
    print(f"{number} is even") # Check if number is even
else:
    print(f"{number} is odd") # Check if number is odd

if number != 0:
    print(f"{number} is non-zero") # Check if number is non-zero
else:
    print(f"{number} is zero") # Check if number is zero

number_2 = 18

if number > number_2:
    print(f"{number} is greater than {number_2}") # Compare two numbers
elif number < number_2:
    print(f"{number} is less than {number_2}") # Compare two numbers
else:
    print(f"{number} is equal to {number_2}") # Compare two numbers

a = 5 # Variable assignment 1
b = 4 # Variable assignment 2

print(a + b) # Addition
print(a - b)   # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a // b) # Floor division
print(a % b) # Modulus

c = a - b # Variable assignment with expression
print(c) # Print the result of subtraction

#1var = 10 # Invalid variable name (starts with a digit)

_var = 20 # Valid variable name (starts with an underscore)
var1 = 30 # Valid variable name (contains digits but does not start with one)
var_2 = 40 # Valid variable name (contains underscore and digits)
varName = 50 # Valid variable name (camel case)

