# map
num = [1,2,3,4,5,6,7,8]
def square (num):
    return num**2
print(square(2))
# map(function, iterables)
# function : lambda x :x**2
# iterables : numbers
map(lambda x :x**2,num) # map() function returns a map object
print(map(lambda x :x**2,num))
# to make it initialize convert it to list 
print()
ex = list(map(lambda x :x**2,num))
print(list(map(lambda x :x**2,num)))
print(ex)


def sqr(num):
 return num * num
print(sqr(10))

lst = [1,2,3,4,5,6,7,8,9]
ans = list(map(sqr,lst))
print(ans)

# lamba function with map
ans = list(map(lambda x: x*x,lst))
print(ans)

print()
num1= [1,2,3]
num2 = [5,6,7]
add =list(map(lambda x,y:x+y, num1,num2))
print(add)

print()
# Conversion
# use map tp convert list of character to int
num = ['1','2','3','4','5']
print(num)
conv=list(map(int,num))
print(conv)

print()
# upper case
fruits = ["apple","banana","cherry is my fav"]
print(fruits)
print(list(map(str.upper,fruits)))
# lower case
print(list(map(str.lower,fruits)))
# Capitalize the first letter of each fruit name
print(list(map(str.capitalize,fruits)))
#  Title case (first letter of each word capitalized)
print(list(map(str.title,fruits)))
# strip
print(list(map(str.strip,fruits)))
# Replace 'a' with 'b'
print(list(map(lambda x:x.replace('a','b'),fruits)))
# splits on whitespace into lists of words
# Each string in the list contains unwanted spaces, tabs (\t), or newlines (\n). 
# The strip() function removes those only from the start and end—not from the middle.
print(list(map(lambda x:x.split(),fruits)))
# joins the original list with spaces into one string
print(' '.join(fruits))

print()
def get_name(person):
    return person['name']

people = [
    {'name': 'John', 'age': 30},
    {'name': 'Alice', 'age': 25},
]

print(list(map(get_name,people)))




"""
Output
4
<map object at 0x102a8c970>

[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64]
100
[1, 4, 9, 16, 25, 36, 49, 64, 81]
[1, 4, 9, 16, 25, 36, 49, 64, 81]

[6, 8, 10]

['1', '2', '3', '4', '5']
[1, 2, 3, 4, 5]

['apple', 'banana', 'cherry is my fav']
['APPLE', 'BANANA', 'CHERRY IS MY FAV']
['apple', 'banana', 'cherry is my fav']
['Apple', 'Banana', 'Cherry is my fav']
['Apple', 'Banana', 'Cherry Is My Fav']
['apple', 'banana', 'cherry is my fav']
['bpple', 'bbnbnb', 'cherry is my fbv']
[['apple'], ['banana'], ['cherry', 'is', 'my', 'fav']]
apple banana cherry is my fav

['John', 'Alice']
(base) niralirajpura@Mac DS % 

"""