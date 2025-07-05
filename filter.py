# filter(function, iterable)
def even(num):
    if num % 2 == 0:
        return True
print(even(24))

lst = [1,2,3,4,5,6,7,8,9]
print(list(filter(even,lst)))

# Filter with lambda funcction
# print only numbers >5
greater_than_5 =list(filter(lambda x : x>5 ,lst))
print("print values greater than five",greater_than_5)

#filter, lambda  and multiple condition
ans =list(filter(lambda x : x>5 and x%2==0 ,lst))
print("print values greater than five and even",ans)

# apply filter in dictionary
print()
people = [
    {'name': 'John', 'age': 10},
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 40},
    {'name': 'Charlie', 'age': 35},
]
def age_check(person):
    return person['age'] > 25

filtered_people = list(filter(age_check, people))
print(filtered_people)


"""
Output
True
[2, 4, 6, 8]
print values greater than five [6, 7, 8, 9]
print values greater than five and even [6, 8]

[{'name': 'Bob', 'age': 40}, {'name': 'Charlie', 'age': 35}]

"""