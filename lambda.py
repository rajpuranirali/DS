# syntax
lambda agruments: expression
# addition function
def add(a,b):
    return a + b
print("Addition: ", add(4,4))

# Convert thi function to lambda
add = lambda a,b:a+b


print("Print type",type(add))
print("\nAddition using lamba function:" , add(4,4))
# user Input
num1 = int(input("Please Enter first number : "))
num2= int(input("Please Enter second number: "))
print("Addition of two numbers is",add(num1,num2))

# Check number is even or not
def even(num):
    if num % 2 == 0:
        return "Number is even"
    else:
            return "Number is odd"

print(even(28))
print(even(33))

# Convert this function to lambda
even= lambda num:num%2==0
print("Number is even: ", even(28))

# Lambda with multiple parameters
add = lambda a,b,c : a+b+c
print("\nAddition of three numbers is",add(4,5,6))

num1=int(input("First number: "))
num2=int(input("Second number: "))
num3=int(input("Third number: "))
print("Addition of three numbers is",add(num1,num2,num3))

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

"""
output
Addition:  8
Print type <class 'function'>

Addition using lamba function: 8
Please Enter first number : 4
Please Enter second number: 10
Addition of two numbers is 14
Number is even
Number is odd
Number is even:  True

Addition of three numbers is 15
First number: 20
Second number: 30
Third number: 40
Addition of three numbers is 90
4
<map object at 0x1051cefd0>

[1, 4, 9, 16, 25, 36, 49, 64]
[1, 4, 9, 16, 25, 36, 49, 64]
"""