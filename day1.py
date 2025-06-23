# this is single line comment 
'''this is multiline comment'''



# Example of Case sensitive 
name = "tom" 
Name = "Jerry" #  both the variables are different identifiers 
print(name) 
print(Name)


print()
#  Indentation:
age = 32
if age > 30:
    print (age)


print()
# line continution 
# use a ('/') to continue the statement to the next line. 
total = 1+2+3+4+5+6+7+\
4+5+6
print (total)


print()
# multiple statement on a single line 
x=5;y=5;z=x+y
print (z)


print()
# semnatics in python 
# variable assignment
age=32
type(age)


print()
# type inference
variable=10
print(type(variable))
variable ="Tom"
print(type(variable))



# Name error 
# a=b  
# NameError: name 'b' is not defined



print()
# code example of indentation
if True:
    print("correct indentation")
    if False:
        print("This will not print")
print("This will Print")


print()
# Declaring and assigning variables
age = 5
height = 2.1
name= "Ram"
is_student= True

print("age: ", age)
print("height: ", height)
print("name: ", name)


print()
# variables must start with letters or (underscore) '_'. 
# variables name are case sensitive. 
#python is dynamically typed, type of variable determined at runtime


first_name = "tom"
_last = "Cruise"
print(first_name)
print(_last)
print(type(is_student))

# type checking and conversion
print("Data type of age: ",type(age))

age_str = str(age)
print("data type of age after type conversion: ", type(age_str)) 

print()
# convert float to int 
height_int = int(height)
print(type(x))
print(height_int)

print()
# convert from float to int 
height_float = float(height_int)
print(type(height_float))
print(height_float)

# Dynamic typing
# python allows the type of variable to change as the program executes.
var = 10
print(type(var))

var =10.1
print(type(var))

var= "Tom"
print(type(var))


print()
# input
age = input("what is your age")
print(age, type(age))
# now type casting
age= float(input("what is your age"))
print(age, type(age))


print()
# calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2
power = num1 ** num2
floor_division = num1 // num2


print("Addition is", sum)
print("Difference is", difference)
print("Product is", product)
print("Quotient is", quotient)
print("Remainder is", remainder)
print("Power is", power)
print("Floor Division is", floor_division)  #int ans only
