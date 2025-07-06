# create a dictionary
empty_dict={}
print(type(empty_dict))

mpty_dic = dict()
print(type(mpty_dic))

# Keys Must Be Unique
print()
studet={"name": "tom" , "age" : 22, "percentage" : 96} #key :value
print(studet)

# Error
# If a key is repeated, the last value overwrites the earlier one.
print()
student = {"name" : "Tom" , "age" :22 , "name":"Jerry"}
print(student)

# Accessing dic elements
print()
student = {"name" : "Tom" , "age" : 20 , "city" : "Chicago" , "Grade" : 'A'}
print(student['name'])

# Accessing Dic get() method
print()
print(student.get('name'))
print(student.get('last_name')) #None
print(student.get('last_name', "Not Available")) # if value is not present write Not Available. 
mark = student.get('marks',"Not Available")
print("marks :" , mark)

print()
# modification Dic elements
print(student)
# update the value for key
student ["age"] = 33
# add key and value
student ["address"] = "USA"
print(student)

print()
# delete key and value
del student['city'] 
print(student)

print()
# pop() method LIFO 
print()
student.pop('Grade')
print(student)

print()
# print all the keys 
dic_keys = student.keys()
print(dic_keys)

print()
# print all the values 
print (student.values()) 

print()
# print all the items
print(student.items())

print()

# copy 
# update will happen in original dic and copied dic to overcome this issue shallow coppy is the solution. 

student_copy = student
print(f"original dic {student}")
print(f"copied dic {student_copy}")
print()
student_copy["age"] = 19
print("modified student_copy" , student_copy) # modified student_copy {'name': 'Tom', 'age': 19, 'address': 'USA'}
print("Student dic ",student) # Student dic  {'name': 'Tom', 'age': 19, 'address': 'USA'}
student_copy["name"] = "Jerry"
print()
print("modified student_copy" , student_copy) # modified student_copy {'name': 'Jerry', 'age': 19, 'address': 'USA'}
print("Student dic ",student) # Student dic  {'name': 'Jerry', 'age': 19, 'address': 'USA'}
print()


# shallow copy
student_shallow_copy = student.copy()

print()
# update 
student_shallow_copy["address"] = "Canada"
print("modified student_shallow_copy" , student_shallow_copy) # modified student_shallow_copy {'name': 'Jerry', 'age': 19, 'address': 'Canada'}
print("Student dic ",student) # Student dic  {'name': 'Jerry', 'age': 19, 'address': 'USA'} 

print()
student["age"] = 22
print("modified student_shallow_copy" , student_shallow_copy) # modified student_shallow_copy {'name': 'Jerry', 'age': 19, 'address': 'Canada'}
print("Student dic ",student) # Student dic  {'name': 'Jerry', 'age': 22, 'address': 'USA'}

# iterating over dictionary
print()
for keys in student.keys(): 
    print(keys)

for val in student.values():
    print(val)


# When you use items() on a dictionary, it gives you a list of all the keys and their matching values, together in pairs.
# item() is a method.
print()
print(student.items())


print()
for key,val in student.items():
    print(f"{key} : {val}")

# Nested Dictionaries
students = { 
    "student1" : {"name":"Tom","age":13} ,
    "student2" : {"name":"Jerry" , "age" : 20 }

}

# Access the Dictionaries 
print()
print(students["student1"]["name"]) # Tom
print(students["student2"]["name"]) # Jerry


# iterating over nested Dictionaries 
print()
print("iterating over nested Dictionaries")
for student_id , student_info in students.items() :
    print(f"{student_id} : {student_info}") # student1 : {'name': 'Tom', 'age': 13} student2 : {'name': 'Jerry', 'age': 20}
    for key, val in student_info.items(): 
        print(f"{key} : {val}")

# student1 : student_id 
# student_info : {'name': 'Tom', 'age': 13}

# Dictionary comphrehension
# Square of a number
print()
squares = {x:x**2 for x in range(5)} #x (key): x**2 (value)
print(squares)

# even numbers
print()
check_even ={x:x%2==0 for x in range(5)}
print(check_even) 

#Conditional Dictionary comphrehension
# if square of a number is even then print
print()
even = { x:x**2 for x in range (5) if x%2== 0 }
print(even)

# Use dictionary to count the frequency of element in the list 
# list of numbers
print()
lst = [1,2,3,4,5,6,1,1,1,1,1,3,3,3,3,4,4,4,4,3,3,3,3,3]
freq = {}
for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

"""
What happens:
freq = {}: We start with an empty dictionary to store the frequency of each number.
for num in lst:: This loop goes through each number in the list lst.
if num in freq:: Checks if the current number is already a key in the dictionary freq.
If it is, increase its count by 1 (freq[num] += 1).
If it isn't, add the number to the dictionary with a count of 1 (freq[num] = 1).
print(freq): After processing each number, the dictionary is printed to show the current frequencies.

"""

"""
OUTPUT
--------------------------------------------

<class 'dict'>
<class 'dict'>

{'name': 'tom', 'age': 22, 'percentage': 96}

{'name': 'Jerry', 'age': 22}

Tom

Tom
None
Not Available
marks : Not Available

{'name': 'Tom', 'age': 20, 'city': 'Chicago', 'Grade': 'A'}
{'name': 'Tom', 'age': 33, 'city': 'Chicago', 'Grade': 'A', 'address': 'USA'}

{'name': 'Tom', 'age': 33, 'Grade': 'A', 'address': 'USA'}


{'name': 'Tom', 'age': 33, 'address': 'USA'}

dict_keys(['name', 'age', 'address'])

dict_values(['Tom', 33, 'USA'])

dict_items([('name', 'Tom'), ('age', 33), ('address', 'USA')])

original dic {'name': 'Tom', 'age': 33, 'address': 'USA'}
copied dic {'name': 'Tom', 'age': 33, 'address': 'USA'}

modified student_copy {'name': 'Tom', 'age': 19, 'address': 'USA'}
Student dic  {'name': 'Tom', 'age': 19, 'address': 'USA'}

modified student_copy {'name': 'Jerry', 'age': 19, 'address': 'USA'}
Student dic  {'name': 'Jerry', 'age': 19, 'address': 'USA'}


modified student_shallow_copy {'name': 'Jerry', 'age': 19, 'address': 'Canada'}
Student dic  {'name': 'Jerry', 'age': 19, 'address': 'USA'}

modified student_shallow_copy {'name': 'Jerry', 'age': 19, 'address': 'Canada'}
Student dic  {'name': 'Jerry', 'age': 22, 'address': 'USA'}

name
age
address
Jerry
22
USA

dict_items([('name', 'Jerry'), ('age', 22), ('address', 'USA')])

name : Jerry
age : 22
address : USA

Tom
Jerry

iterating over nested Dictionaries
student1 : {'name': 'Tom', 'age': 13}
name : Tom
age : 13
student2 : {'name': 'Jerry', 'age': 20}
name : Jerry
age : 20

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

{0: True, 1: False, 2: True, 3: False, 4: True}

{0: 0, 2: 4, 4: 16}

{1: 6, 2: 1, 3: 10, 4: 5, 5: 1, 6: 1}




"""