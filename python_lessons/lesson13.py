#functions

"""

def function1(statement1):
    "
    This is a function that prints a statement.
    "
    print(statement1 ,"is a good programming language.")

function1("Python")

"""

"""""

def example_function(name,age):
    print(f"Hello, {name}! You're {age} years old.")

example_function(input("Enter your name: "), input("Enter your age: ")) #function with parameters

"""""

"""

def function2(statement2= "Istanbul"):
    print(statement2, "is a beautiful city.")

function2() #function with default parameter
function2("Ankara") #function with argument
function2(statement2="Izmir") #function with keyword argument

"""

def math_operations(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    if b != 0:
        div_result = a / b
    else:
        div_result = "undefined (division by zero)"
    return sum_result, diff_result, prod_result, div_result

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
results = math_operations(a, b)
print(f"Sum: {results[0]}, Difference: {results[1]}, Product: {results[2]}, Division: {results[3]}")