mark = int (input("Please Enter your marks: "))

if mark >=90:
    print("Grade A")
elif mark >=80 and mark <90 :
    print("Grade B")
else:
    print("Sorry!! You are failed!!")

# Nested Condition Statement 
number= int(input("Please Enter Number: "))

if number > 0:
    if number % 2 == 0:
        print(number,"is Even number")
    else:
        print(number,"is Odd number")
else:
    print(number,"is Negative number")

# Leap year 
"""Python Logic:
If a year is divisible by 400, it is a leap year.
If a year is divisible by 4, and not divisible by 100, it is a leap year.
If a year is divisible by 100, and not divisible by 400, it is not a leap year.
 """

year = int(input("Enter year: "))
if year % 400 == 0:
    print(year,"is a leap year")
elif(year % 4 ==0) and (year%100 != 0):
    print(year,"is a leap year")
elif (year % 100 ==0 ) and (year % 400 != 0):
    print(year,"is not a leap year")
else:
    print(year,"is not a leap year")

# leap year using nested if else

if year % 400 == 0:
    print(year, "is a leap year")
else:
    if year % 100 == 0:
        print(year, "is not a leap year")
    else:
        if year % 4 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")

# Calculator using  if else
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(num1 + num2)
elif operator == "-" :
    print(num1 - num2)
elif operator == "*" :
    print(num1 * num2)
elif operator == "/":
    print(numb1/num2)
else:
    print("Invalid operator")



"""
output
Please Enter your marks: 46
Sorry!! You are failed!!
Please Enter Number: 11
11 is Odd number
Enter year: 2025 
2025 is not a leap year
2025 is not a leap year
Enter first number 10
Enter second number 10 
Enter operator (+, -, *, /): +
20.0
"""


print()
# loops
print("Display range range(5) : ")
i = range(5)
print(i)
# Note that range(5) is not the values of 0 to 5, but the values 0 to 4.
# it does not display 5.
print("Display value of 0 to 4: ")
for i in range(5):
    print(i)

print()
print("Display value of 1 to 5: ")

print()
for i in range(1,6): # it will display 1 to 5
    print(i)

# start from 1 to 10 and incremented by 2. value is 1 to 9.
print()
print("display odd numbers from 1 to 10: ") # incremented by 2. 
for i in range (1,10,2):
    print(i)

print("Display 10 to 2")
for i in range (10,1,-1):
    print(i)

# It goes through each character in the string one by one.
# The variable i takes on the value of each character in the string, in order.
print("String for loop")
string = "Sita Ram"
for i in string:
    print(i)

# while loop
count = 0
count = int(input("Enter value of Count: "))
while count < 5:
    print(count)
    count = count + 1

# break
# break Statement:
# Purpose: Terminates the loop entirely.
# Effect: Exits the loop as soon as the break statement is executed, even if the loop condition is still true.
# it will display 0 to 4 
print()
print("Break statement")
for i in range (10): 
    if i == 5:
        break
    print(i)

# continue
#  Does not terminate the loop; it just skips the code after continue for the current iteration.
# When you want to skip a case
# it will display odd numbers. 
print()
print("Example of Continue ")
for i in range(10):
    if(i%2==0):
        continue
    print(i)
    
# pass
# It means: “do nothing.”
# It's a placeholder when code is required, but you don't want to write anything yet.
for i in range(5):
    if i == 3:
        pass  # Do nothing when i is 3
    print(i)

def my_function():
    pass
# Writing code later (like a "to-do")

# nested loop
# An f-string lets you easily insert variables into a string using {}.
for i in range(3):
    for j in range(2):
        print(f"i: {i} and j: {j}")
# addition of 1 to 10

n = 1
sum = 0
while n<=10:
    sum = sum + n
    print(f"{sum}+{n}={sum}")
    n = n+1
print(sum)

print()
# ask user for input
n = 1
m = int(input("Enter the value for addition: "))
sum = 0
while n<=m:
    sum = sum + n
    print(f"{sum}+{n}={sum}")
    n = n+1
print("total sum of given number is " , sum)


# for loop
print()
sum = 0
n = int(input("Enter value you want to add till : ")) 
for i in range(1,n+1 ): # n = 10, range is 1 to 9. 
    sum = sum + i
    print(f"{sum}+ {i} = {sum}")

# prime number




    