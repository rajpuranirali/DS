# Unpacking tuples with default values

# print empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

print()

# convert list to tuple
print("convert list to tuple")
my_list = [10, 20, 30]
print(type(my_list), my_list)

my_tuple = tuple(my_list)
print( type(my_tuple),my_tuple,)       

print()

# convert tuple to list
print("convert tuple to list")

my_tuple = (1, 2, 3, 4)
print(my_tuple, type(my_tuple))

my_list = list(my_tuple)
print(my_list, type(my_list))

print("Mixed Tuples")       
mixed_tuples = ("Start", 1,2,"hello", True, 'end')
print(mixed_tuples)

# Accesing tuples
number = (1,2,3,4,5,6,7,8)
print(number)
print(number[0])
print(number[-1])
print(number[1:4])
print(number[::])
print(number[::-1])

# Tuples Operation
# Concatination
concat_tuples = mixed_tuples + number
print(concat_tuples)

# Repetation
repeated_tuples = mixed_tuples * 3
print(repeated_tuples)
print()

reperated_tuples_numbers = number *3 
print(reperated_tuples_numbers)
print()

# Once tuple is created you can not change it as its immutable. 

numbers=(1,2,4,3,4,5,6)
tcount = numbers.count(4)
print(f"Count 4 in tuple{tcount}")
print()

tindex =number.index(1)
print(f"index of number in tuple {tindex}")
print()

# Tuple Packing
packed_tuple = 1,2,"hello",3.14
print(packed_tuple)
print() 
# Tuple Unpacking
a,b,c,d = packed_tuple
print(a)
print(b)
print(c)
print(d)
print()

# Unpacking tuples with star
numbers = (1,2,3,4,5,6)
first, *middle , last = numbers
print(first)
print(middle)
print(last)
print()

# Unpacking tuples with double star
numbers = (1,2,3,4,5,6)
*middle, last = numbers
print(middle)
print(last)
print()

# list contain tuple
lst = [[1,2,3],[4,5,6],[7,8,8,9,10,19],(2,"hello",True,'p')]
print(lst)
print()

# Nested tuples 
tpl = ((1,2,3),(4,5,6),(7,8,8,9,10,19),(2,"hello",True,'p'))
print(tpl)
print(tpl[0])
print(tpl[1][1])
print(tpl[2][1:4])
print()

# Iteration over nested tuples
for sub_tpl in tpl:
    for item in sub_tpl :
        print(item, end = " ")
        print()

"""
OUTPUT
()
<class 'tuple'>

convert list to tuple
<class 'list'> [10, 20, 30]
<class 'tuple'> (10, 20, 30)

convert tuple to list
(1, 2, 3, 4) <class 'tuple'>
[1, 2, 3, 4] <class 'list'>
Mixed Tuples
('Start', 1, 2, 'hello', True, 'end')
(1, 2, 3, 4, 5, 6, 7, 8)
1
8
(2, 3, 4)
(1, 2, 3, 4, 5, 6, 7, 8)
(8, 7, 6, 5, 4, 3, 2, 1)
('Start', 1, 2, 'hello', True, 'end', 1, 2, 3, 4, 5, 6, 7, 8)
('Start', 1, 2, 'hello', True, 'end', 'Start', 1, 2, 'hello', True, 'end', 'Start', 1, 2, 'hello', True, 'end')

(1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8)

Count 4 in tuple2

index of number in tuple 0

(1, 2, 'hello', 3.14)

1
2
hello
3.14

1
[2, 3, 4, 5]
6

[1, 2, 3, 4, 5]
6

[[1, 2, 3], [4, 5, 6], [7, 8, 8, 9, 10, 19], (2, 'hello', True, 'p')]

((1, 2, 3), (4, 5, 6), (7, 8, 8, 9, 10, 19), (2, 'hello', True, 'p'))
(1, 2, 3)
5
(8, 8, 9)

1 
2 
3 
4 
5 
6 
7 
8 
8 
9 
10 
19 
2 
hello 
True 
p 



"""