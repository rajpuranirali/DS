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

# pop() method
print()
student.pop('Grade')
print(student)
