# Temprature conversion 
def tempcov(temp ,unit):
    if unit == 'C':
        return ((temp *(9/5))+32)
    elif unit == 'F':
        return ((temp-32)*(5/9))
    else:
        return "Invalid unit"
    
u = tempcov(24,'C')
print(u)

temp = float(input("Please Enter temprature: "))
unit = input("Please Enter unit (C/F): ")
print(tempcov(temp,unit)) 

# Password Streght Checker
