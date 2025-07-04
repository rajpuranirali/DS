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

