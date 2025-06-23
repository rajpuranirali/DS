# this is single line comment 
'''this is multiline comment'''



# Example of Case sensitive 
name = "tom" 
Name = "Jerry" #  both the variables are different identifiers 
print(name) 
print(Name)



#  Indentation:
age = 32
if age > 30:
    print (age)



# line continution 
# use a ('/') to continue the statement to the next line. 
total = 1+2+3+4+5+6+7+\
4+5+6
print (total)



# multiple statement on a single line 
x=5;y=5;z=x+y
print (z)



# semnatics in python 
# variable assignment

age=32
type(age)


# type inference
variable=10
print(type(variable))
variable ="Tom"
print(type(variable))



# Name error 
# a=b  
# NameError: name 'b' is not defined




# code example of indentation
if True:
    print("correct indentation")
    if False:
        print("This will not print")
print("This will Print")
