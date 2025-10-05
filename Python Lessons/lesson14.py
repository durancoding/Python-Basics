#lambda expressions
#lambda is the function without a name

""""

lambda x: x + 10
add_ten = lambda x: x + 10
input_number = float(input("Enter a number: "))
print(add_ten(input_number)) #basic usage of lambda

"""

"""
def add_ten(x):
    return x + 10

input_number = float(input("Enter a number: "))
print(add_ten(input_number)) #basic usage of function without lambda

"""

european_cities = ["Paris", "Berlin", "Madrid", "Rome", "Vienna"]

number_city = lambda idx, city: f"{idx} - {city}"

for i in range(len(european_cities)):
    print(number_city(i + 1, european_cities[i]))

print(list(filter(lambda num : num %2 == 0, range(1,20)))) #filter function with lambda

