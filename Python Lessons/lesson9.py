#tuples , sets and booleans

tuple1 = (1,2,3,4,5)
print(tuple1)
print("First element:", tuple1[0])  # Accessing first element

#tuple1[0] = 10  # This will raise an error since tuples are immutable

set1 = {1,2,3,4,5}
print(set1)
set1.add(6)  # Adding an element
set1.add(3)  # Adding a duplicate element (will have no effect)
print(set1)

print(True)  # Boolean values
print(False)
print(5 > 3)  # Comparison resulting in boolean

print(1 in set1)  # Checking membership in set
print(2 in tuple1)  # Checking membership in tuple

new_list = [1,2,2,3,4,4,5]
print(len(new_list))  # Length of the list
unique_set = set(new_list)  # Converting list to set to remove duplicates
print(len(unique_set))  # Print the set with unique elements
print(1 in unique_set)  # Checking membership in the new set

