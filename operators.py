#Arithmetic Operations
# + , - , * , / , //
# a=5
# b=10
first_number= float(input("Enter first number:" ))
second_number = float(input("Enter Second number"))

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number /second_number
floor_division = first_number // second_number # floor division discards the decimal part 

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(floor_division)


print()
# comparision operators
# If the two values are equal, it returns True; otherwise, it returns False.
# compare, greater than, less than, greater than equal to , less than equal to, not equal to 
str1 = str(input("Enter first String: "))
str2 = str(input("Enter Second String : "))
comparision_operator = str1 == str2
comparision_operator = first_number == second_number 

print("comparision of string" ,comparision_operator)
print("comparision of numbers" ,comparision_operator)

# greater than 
greater_than = first_number > second_number
print("first number is greater than second number " ,greater_than)

# less_than = first_number < second_number
# print(less_than)

less_than = first_number < second_number
print("first number is less than second number " ,less_than)

greater_than_or_equal_to = first_number >= second_number
print(first_number, "is greater than and equal to" , second_number , ":" ,greater_than_or_equal_to)

less_than_or_equal_to = first_number <= second_number
print(first_number, "is less than and equal to" , second_number , ":" ,less_than_or_equal_to)

not_equal_to = str1 != str2
print(str1, "is not equal to" , str2 , ":" ,not_equal_to)

# Logical operators
# AND, OR, NOT
'''
#and : Returns True if both expressions are true
#or: returns True if at least one of the expressions is True. If both expressions are False, it will return False.
#not: if the expression is True, applying not will make it False. If the expression is False, applying not will make it True ; inverts the value. 

'''
# and 
# Returns True if both expressions are true 
print()

a = 10
b = 20
c= 30 

print("a=10" , "\n", "b=20" , "\n" , "c=30" )
result = a and b
print (result)

if ((a < b) and  (a < c)) :
    print("And operator example" "\n", "true")


# OR
# returns True if at least one of the expressions is True. If both expressions are False, it will return False.
if((a<b) or (b>c)) :
    print("OR operator example" "\n", "true") #true

if((a<b) or (a<c)) :
    print("OR operator example" "\n", "true") # true

if((a>b) or (a>c)) :
    print("OR operator example" "\n", "true") # true
else: 
    print("OR operator example" "\n", "false") # false



#  NOT
# if the expression is True, applying not will make it False. If the expression is False, applying not will make it True ; inverts the value. 
result = not( a < b)
print("Example of not" ,result)

# a<b is True, so applying not to True makes it false.


"""
Enter first number: 100
Enter Second number 3
103.0
97.0
300.0
33.333333333333336
33.0

Enter first String: Tom
Enter Second String : tom
comparision of string False
comparision of numbers False
first number is greater than second number  True
first number is less than second number  False
100.0 is greater than and equal to 3.0 : True
100.0 is less than and equal to 3.0 : False
Tom is not equal to tom : True

a=10 
 b=20 
 c=30
20
And operator example
 true
OR operator example
 true
OR operator example
 true
OR operator example
 false
Example of not False

"""
