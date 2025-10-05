#lists

list1 = [1,2,3,4,5]
list2 = ["Hello", 1, 2.5, True]

print("List1:", list1)
print("List2:", list2)

list1.append(6) #add element to the end of the list
print("List1 after append:", list1)

print("Item popped from List1:", list1.pop()) #remove and return the last item

list3 = ["A","B","C","D","E"]

print("First item of list3:", list3[0]) #indexing
print("Everything after the first item of list3:", list3[1:]) #slicing from index 1 to the end
print("Slice from index 1 to index 4 (not included) of list3:", list3[1:4]) #slicing from index 1 to index 4 (not included)

list4 = ["Gta", "Fifa", "Minecraft", "Zelda"]
print("List4 before modification:", list4)
list4[0] = "Cyberpunk" #modifying the first item
print("List4 after modification:", list4)

example_list = [1,2,[3,4,5]]
print(example_list[2]) #accessing nested list
print("Accessing nested list item:", example_list[2][1]) #accessing nested list item

example_list_2 = [1,2,3,["A","B","C",["D","E","F"]]]
print("Accessing deeper nested list item:", example_list_2[3][3][1]) #accessing deeper nested list item
