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

