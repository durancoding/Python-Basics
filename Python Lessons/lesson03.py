#typecasting = converting one data type to another data type like int to str or str to int
#str() , int() , float() , bool()

city = "Istanbul"
population = 15000000.5
area = 5461
is_city = True

print(type(city)) # <class 'str'>
print(type(population)) # <class 'int'>
print(type(area)) # <class 'float'>
print(type(is_city)) # <class 'bool'>

population = int(population) # float to int 
print(type(population)) # <class 'int'> we converted float to int
print(population) # 15000000

area = float(area) # int to float
print(type(area)) # <class 'float'> we converted int to float
print(area) # 5461.0

area += 0.5 # area = area + 0.5
print(area) # 5461.5

is_city = str(is_city) # bool to str
print(type(is_city)) # <class 'str'> we converted bool to str
print(is_city) # True