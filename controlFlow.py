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

year= int(input("Enter year: "))
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