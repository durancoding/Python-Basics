#input fuction
name = input("Enter your name: ") # Taking name as input from user
age = input("Enter your age: ") # Taking age as input from user

print(f"Hello, {name}! You are {age} years old.") # Using f-string for formatted output

if name == "Alice":
    print("Welcome back, Alice!") # Checking if name is Alice
elif name == "Bob":
    print("Hey Bob, good to see you!") # Checking if name is Bob
else:
    print(f"Nice to meet you, {name}!") # Greeting for other names

