# create a set
my_set= {1,2,3,4,5}
print(my_set, type(my_set))
print()


# empty set
empty = set()
print(empty, type(empty))
print("add in empty set:")
empty.add(2)
print(empty) 

#create an empty dictionary
print()
empty_dictionary = {}
print(type(empty_dictionary))  # Output: <class 'dict'>



print()
set_test = {1,2,3,4}
add = set_test.add(10)
print(set_test) # {1, 2, 3, 4, 10}
print(add , set_test) # None {1, 2, 3, 4, 10}




# Use list to create a set
print()
my_set = set([1,2,3,4,5])
print(my_set, type(my_set))


print()
Duplicate_value_set = set([1,2,3,4,5,5,5,5,4,4,4,5,2,3,]) #output: {1, 2, 3, 4, 5} <class 'set'>
print(Duplicate_value_set, type(Duplicate_value_set))

# basic set operations:
my_set.add(7)
print(f"add an element 7:{my_set}")
# remove elements 

# discard() and remove() will remove element. remove() will raise error if element does not exist and  discard() does nothing. 
my_set.remove(3)
print(f"remove 3: {my_set}")
# discard an element
my_set.discard(5)
print(f"discard 5: {my_set}")

# pop:  first value of the set will removed 
poped_element = my_set.pop()
print(f"poped element: {poped_element}")
print(f"set after pop: {my_set}")

# clear all the ekement 
my_set.clear()
print(f"set after clear: {my_set}")
print()

# Set membership test
my_set = {1,2,3,4,5}
a = 1 in my_set
print(a)
print(10 in my_set)
print(f"{2 in my_set}")

# mathemetical operation 
# union
print()
set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1.union(set2)
print("union:", union_set)

# intersection
print()
print("intersection ")
intersection_ = set1.intersection(set2)
print(intersection_) # Returns common elements. 

# intersectionupdate
# It keeps only the common elements between sets and changes the original set.
print()
set1_update = set1.intersection_update(set2)
print("set1 is",set1)
print("set2 is",set2)

print()
set1 = {1,1,2,3,8,9}
set2 = {3,4,5,6,7}
# diffrence 
# it will display element presence is set1 but not in set2 
print(f"set1 : {set1} ...... set2 {set2}")
difference_set = set1.difference(set2)
print("difference:", difference_set) # difference: {8, 1, 2, 9}

# symmetric difference 
# unique element from both the side 
# remove common element from both the side. 

print("symmetric difference:", set1.symmetric_difference(set2)) # symmetric difference: {1, 2, 4, 5, 6, 7, 8, 9} 

# set methods
# all the elements from set1 is exist in set 2 or not 
print("Check subset set:", set1.issubset(set2))
print("Check superset set:", set1.issuperset(set2))

A = {1, 2}
B = {1, 2, 3, 4}
print(f"set A : {A} .... set B :  {B}")
print("is set A  subset of B:" , A.issubset(B))  # 👉 True check A is inside B ? true
print("is set A  superset of B:" , A.issuperset(B)) # A contains all the elements of B ? false
print("is set A  equal to B:" , A == B) # 👉 False 

print()
# if I want to delete duplicate of list 
lst = [1,2,3,4,4,5]
con= set(lst)
print(con)

# count unique characters from text
text = "hello world hello world hello world"
print(text)
# words= text.split()
unique_word = set(text)
print(unique_word)
count_unique = len(unique_word)
print(count_unique)

text2= "my name is tom"
print(text2)
# words= text.split()
unique_word2 = set(text2)
print(unique_word2)
count_unique2= len(unique_word2)
print(count_unique2)


# count unique words from text
text = "hello world hello world hello world"
print(text)
text= text.split()
unique_word = set(text)
print(unique_word)
count_unique = len(unique_word)
print(count_unique)

text2= "my name is tom and tom"
print(text2)
text2= text2.split()
unique_word2 = set(text2)
print(unique_word2)
count_unique2= len(unique_word2)
print(count_unique2)

"""

{1, 2, 3, 4, 5} <class 'set'>

set() <class 'set'>
add in empty set:
{2}

<class 'dict'>

{1, 2, 3, 4, 10}
None {1, 2, 3, 4, 10}

{1, 2, 3, 4, 5} <class 'set'>

{1, 2, 3, 4, 5} <class 'set'>
add an element 7:{1, 2, 3, 4, 5, 7}
remove 3: {1, 2, 4, 5, 7}
discard 5: {1, 2, 4, 7}
poped element: 1
set after pop: {2, 4, 7}
set after clear: set()

True
False
True

union: {1, 2, 3, 4, 5, 6}

intersection 
{3, 4}

set1 is {3, 4}
set2 is {3, 4, 5, 6}

set1 : {1, 2, 3, 8, 9} ...... set2 {3, 4, 5, 6, 7}
difference: {8, 1, 2, 9}
symmetric difference: {1, 2, 4, 5, 6, 7, 8, 9}
Check subset set: False
Check superset set: False
set A : {1, 2} .... set B :  {1, 2, 3, 4}
is set A  subset of B: True
is set A  superset of B: False
is set A  equal to B: False

{1, 2, 3, 4, 5}
hello world hello world hello world
{'h', 'w', 'e', 'l', 'r', 'o', ' ', 'd'}
8
my name is tom
{'m', 'y', 'i', 'e', 's', 'o', ' ', 'n', 't', 'a'}
10
hello world hello world hello world
{'hello', 'world'}
2
my name is tom and tom
{'my', 'name', 'tom', 'and', 'is'}
5



"""