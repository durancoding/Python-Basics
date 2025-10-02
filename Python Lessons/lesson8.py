#dictionary

dictionary1 = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(dictionary1)
print(dictionary1['name'])  # Accessing value by key

dictionary2 = {"first":[1,2,3], "second":(4,5,6), "third":{7,8,9}}
print(list(dictionary2.keys()))  # Getting all keys
print(list(dictionary2.values()))  # Getting all values

print('age' in dictionary1)  # Checking if key exists
print(dictionary1.get('age'))  # Safe access to value by key
print(dictionary2['first'][1])  # Accessing nested list element