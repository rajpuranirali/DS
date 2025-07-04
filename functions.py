# create funcation 
def create_funcation (parameter):
    """Doc string """ 
    # function body
    return expression 

# odd or even 
def check_number(num):
    """This Function finds Even or Odd """
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

check_number(24) # Function call

check= int(input("\n" + "Please enter an Number: "))
check_number(check)

# Function with multiple parameters
def add (num1,num2):
    """This function add two numbers"""
    return (num1 + num2)
result = add(2,3)
print("\n" +"Addition of two numbers are" , result)

number1  = int(input("First Number is: "))
number2 = int(input("Second Number is: "))
addition = add(number1,number2)
print(addition )

# same function with 
num1  = int(input("First Number is: "))
num2 = int(input("Second Number is: "))
add = add(num1,num2)
print(addition )

# Greeting Function
def greet(name = "Tom"):
    print(f"Hello, {name}")

greet()
greet("Jerry")  #Overwrites function parameter

# Variable lenght argument 
# Positional and keyword argument

def print_number(*tom): # *tom means the function will take any number of values you give it.
    for num in tom:
        print(num)
print_number(1,2,3,4,5,6,7,8,9,"tom")

# Positional Arguments
def print_memebrs (*args):
    for numbers in args:
        print(numbers)

print_memebrs(1,2,3,4,5,6,7,8,9,"jerry")

# Keywords Argument
def print_details (**args):
    for key, val in args.items():   
         print(f"{key} : {val}")

print_details(name ="Tom", age = 19, country = "USA")

# *args: Collects any number of positional arguments into a tuple.
# **kwargs: Collects any number of keyword arguments into a dictionary.

def details(*args, **kwargs):
    print("Positional Arguments:")
    for val in args:
        print(f"  - {val}")
    
    print("\nKeyword Arguments:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Function call
details(1, 2, 3, 4, name="Tom", age="3", country="USA")

"""
Yes, you can write multiple return statements in a single function, but only one will execute per call — specifically, the first one that runs. 
Once a return statement is executed, the function exits immediately, and no further lines in that function are run.

"""
# return Statements:
def mul(a,b):
    return a*b,a
    return a*b
print(mul)  
ans= mul(2,6)
print(ans)


"""
output

The number is even

Please enter an Number: 30
The number is even

Addition of two numbers are 5
First Number is: 30
Second Number is: 20
50
First Number is: 1
Second Number is: 3
50
Hello, Tom
Hello, Jerry
1
2
3
4
5
6
7
8
9
tom
1
2
3
4
5
6
7
8
9
jerry
name : Tom
age : 19
country : USA
Positional Arguments:
  - 1
  - 2
  - 3
  - 4

Keyword Arguments:
name : Tom
age : 3
country : USA
<function mul at 0x102c95d30>
(12, 2)




"""