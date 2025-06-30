
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

print()
# slicing list:
# list[start:stop:step]



numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(numbers[:]) # print all the elements
print(numbers[2:5]) # [3,4,5]
print(numbers[:5]) #[1,2,3,4,5]
print(numbers[5:]) #[6,7,8,9,10]
print(numbers[::-1]) #[10,9,8,7,6,5,4,3,2,1]
print(numbers[::2]) 
# [1, 3, 5, 7, 9] 
# In numbers[::2]:
# start is omitted → starts from index 0 (1)
# stop is omitted → goes till the end
# step is 2 → selects every second element

# iteration in list 
print()
for numbers in numbers:
    print(numbers) # print all the elements in the list

fruits = ["mango", "banana","apple","orange","kiwi"]
for fruit in fruits:    
    print(fruit) # print all the elements in the list

# print(type(number))
# for index,number in enumerate(numbers):
#     print(index, numbers)

numbers = [10, 20, 30, 40]

for index, number in enumerate(numbers):
    print(index, number)



# Using list comprehension
print() 
# square using for loop
print ("using for loop")
squares = []
for x in range(5):
    squares.append(x**2)
    print(squares)

# Using list comprehension
print("using list comprehension: ")
squares = [x**2 for x in range(5)]
print(squares)

print()
print()
#for loop 
#  lst comprehension for x power 2 
lst = []
for x in range (10):
   lst.append(x**2)
   print(lst)
print()

# print even number
lst = []
for x in range (10):
    if x % 2 == 0: 
        print(x)

print()
even = [print(x) for x in range(10) if x%2==0]  # [expression for item in iterable if condion] 

print()
# nested iteration
list1 = [1,2,3,4]
list2 = ["a","b","c","d"]

list3 = [ print(i,j) for i in list2 for j in list1 ] #[expression for item1 in iterable1 for item2 in iterable2]


print()
# list comprehension with function call
words = ["helllo" , "world" , "are" , "you" ,"okay"]
print(words)
lenghts = [print(len(word)) for word in (words)]

print()
# convert into list using inbuilt function:
lst = list()
print(lst)
print(type(lst))

print()
print("Create a tuple: ")
tpl = tuple = (1,2,3,4)
print(tpl)
print(type(tpl))
# conver it into list 
print("convert tuple in to list using inbuilt function")
lst = list(tpl)
print(lst)
print(type(lst))

print()


# another method convert tuple in list 
tuple = (5,6,7,8)
print(tuple, type(tuple))
print()

lst = list((5,6,7,8))
print(lst, type(lst))

# Nested List
nested_list = [[1,2,3],[4,5,6],[7,8,8,9,10,19],[2,"hello",True,'p']]
print(nested_list)
print(type(nested_list))
print(nested_list[1])
print()
# Slice in nested list
print(nested_list[0][1]) # it will display list of 0th index -> 1 index elememt
print(nested_list [0] [0:3])
print()

# list contain tuple
lst = [[1,2,3],[4,5,6],[7,8,8,9,10,19],(2,"hello",True,'p')]
print(lst)


"""

output
<class 'list'>
['sita', 'Gita', 1, 2, 3, ' ', 4, 'hello']
['sita', 'Gita', 1, 2, 3, ' ', 4, 'hello', True]

display fruits:  ['mango', 'banana', 'kiwi', 'apple']
Display element on zero index:  mango
Display element on first index: banana

Print fruits from idex 1:  ['banana', 'kiwi', 'apple']
Print fruits from index 1 to 3:  ['banana', 'kiwi']
Print last element:  apple
Print last element:  ['apple', 'kiwi', 'banana']

Current list is :  ['mango', 'banana', 'kiwi', 'apple']
modify 2nd element of list:  ['mango', 'papaya', 'kiwi', 'apple']

change string after first element:  ['mango', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']

append method:  ['mango', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n', 'Orange']

insert method:  ['mango', 'banana', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n', 'Orange']

remove method:  ['mango', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n', 'Orange']

pop method:  Orange
Updated list ['mango', 'w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']

Updated fruits :  ['mango', 'w', 'a', 'apple', 't', 'e', 'r', 'm', 'e', 'l', 'apple', 'o', 'n', 'kiwi']

Index number of Kiwi is 13
Count the number of apple in the list 2

Sorted list:  ['a', 'apple', 'apple', 'e', 'e', 'kiwi', 'l', 'm', 'mango', 'n', 'o', 'r', 't', 'w']

Reversed list:  ['w', 't', 'r', 'o', 'n', 'mango', 'm', 'l', 'kiwi', 'e', 'e', 'apple', 'apple', 'a']

List after removing all items:  []

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[3, 4, 5]
[1, 2, 3, 4, 5]
[6, 7, 8, 9, 10]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
[1, 3, 5, 7, 9]

1
2
3
4
5
6
7
8
9
10
mango
banana
apple
orange
kiwi
0 10
1 20
2 30
3 40

using for loop
[0]
[0, 1]
[0, 1, 4]
[0, 1, 4, 9]
[0, 1, 4, 9, 16]
using list comprehension: 
[0, 1, 4, 9, 16]


[0]
[0, 1]
[0, 1, 4]
[0, 1, 4, 9]
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25, 36]
[0, 1, 4, 9, 16, 25, 36, 49]
[0, 1, 4, 9, 16, 25, 36, 49, 64]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

0
2
4
6
8

0
2
4
6
8

a 1
a 2
a 3
a 4
b 1
b 2
b 3
b 4
c 1
c 2
c 3
c 4
d 1
d 2
d 3
d 4

['helllo', 'world', 'are', 'you', 'okay']
6
5
3
3
4

[]
<class 'list'>

Create a tuple: 
(1, 2, 3, 4)
<class 'tuple'>
convert tuple in to list using inbuilt function
[1, 2, 3, 4]
<class 'list'>

(5, 6, 7, 8) <class 'tuple'>

[5, 6, 7, 8] <class 'list'>


[5, 6, 7, 8] <class 'list'>
[[1, 2, 3], [4, 5, 6], [7, 8, 8, 9, 10, 19], [2, 'hello', True, 'p']]
<class 'list'>
[4, 5, 6]

2
[1, 2, 3]

[[1, 2, 3], [4, 5, 6], [7, 8, 8, 9, 10, 19], (2, 'hello', True, 'p')]
"""