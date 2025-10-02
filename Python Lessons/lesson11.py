#loops
#while loop

i = 1
while i <= 5:
    print("Iteration:", i)
    i += 1  # Increment i by 1
else:
    print("While loop completed all iterations.")

#for loop

list1 = [10, 20, 30, 40, 50]
for idx, item in enumerate(list1, start=1):
    print(f"Item_{idx} :", item)
else:
    print(f"Your loop has {idx} iterations.")

list2 = [1,2,3]

for item in list2:
    print("Hey!")

#range function

for i in range(1, 6):  # From 1 to 5
    print("Range iteration:", i)
else:
    print("Range loop completed all iterations.")

print(list(range(5)))  # This will print the range object

for i in range(1, 11, 2):  # From 1 to 10 with step of 2
    print("Range with step:", i)

numb1 = [1,2,3,4,5]

power_of_numb1 = [num**2 for num in numb1]  # List comprehension to square each number
print("Squared numbers:", power_of_numb1)

numb2 = range(1, 11)
power_of_numb2 = [num**3 for num in numb2 if num % 2 == 0]  # Cubes of even numbers
print("Cubes of even numbers:", power_of_numb2)

