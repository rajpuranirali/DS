# List is mutable collection of items.
lst=[]
print(type(lst))

names = ["sita", "Gita",1,2,3," ",4,"hello"]
print(names)

names_mixed = ["sita", "Gita",1,2,3," ",4,"hello", True]
print(names_mixed)

# accessing the elements in list
print()
fruits = ["mango", "banana","kiwi","apple"]
print("display fruits: ", fruits)
print("Display element on zero index: ",fruits[0])
print(f"Display element on first index: {fruits[1]}")

print()
print("Print fruits from idex 1: ",fruits[1:])
print("Print fruits from index 1 to 3: ",fruits[1:3])
print("Print last element: " ,fruits[-1])

# print last 3 elements in list
# -1 refers to the last element in the list.
# -4 refers to one index before the first element in the specified range.
# The -1 after the colon specifies that we want to go backward through the list.
print("Print last element: " ,fruits[-1:-4:-1])




print()
# modify list elements:
print("Current list is : ", fruits)
fruits[1]= "papaya"
print("modify 2nd element of list: ", fruits)

print()
# change after first element in string
fruits[1: ] = "watermelon"
print("change string after first element: " ,fruits)

# List methods 
# append theb  list (generally it insert item at the end of the list)
print()
fruits.append("Orange")
print("append method: ", fruits)

# insert item at specific position
print()
fruits.insert(1,"banana")   
print("insert method: ", fruits)

# remove item from list
print()
fruits.remove("banana")
print("remove method: ", fruits)

print()
# remove the last element from list
pop_fruits = fruits.pop()
print("pop method: ", pop_fruits)
print("Updated list", fruits)

print()
fruits.append("kiwi")

fruits.insert(3,"apple")
fruits.insert(10,"apple")
print("Updated fruits : ", fruits)


# index of an element in the list
print()
find_index = fruits.index("kiwi")
print("Index number of Kiwi is" , find_index)

# Count the specific element in the list]
count_fruits = fruits.count("apple")
print("Count the number of apple in the list",count_fruits)

# sort the list in accending order
print()
fruits.sort()
print("Sorted list: ", fruits)

# reverse the string
print()
fruits.reverse()
print("Reversed list: ", fruits)

# remove all the itema from the list
print()
fruits.clear()
print("List after removing all items: ", fruits)