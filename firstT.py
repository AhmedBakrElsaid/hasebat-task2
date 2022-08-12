# Create a Boolean variable named x
x = True

# Create an integer variable named y
y = 7

# Create a float variable named z
z = 12.5

# Create a string variable names s
s = "Ahmed Bakr"

# Convert the int variable to float
y = float(y)

# Can we convert the str to int ? NO

# Create a list of numbers from 1 to 5
l = [1,2,3,4,5]

# Create a tuple from 10 to 15
t = (10,11,12,13,14,15)

# Convert the list to tuple
l = tuple(l)

# Create a dict of 3 values
d = {'name':'Ahmed','Age':21,"country":"Egypt"}

# Can we use semi colon ; with python
# yes , no problem

# Python is interpreted or compiled ? interpreted

# What is the differences between low level & high level
# low level is machine language is the last step to make machine be able to understand code
# high level is easer to people to understand using programming langeage like python using compiler or interpreter

# What is the differences between = , ==
# = using ti asign variable to its value but == is a comparison operator 

# What do we mean by using !=   NOT EQUAL it is a comparison operator

# What is the operator precedence
#  ++|--  ()  **  *|/  +|-

# Create a variable x with value of 10
x = 10

# Increase x value by 15 using assignment operators
x = x + 15           # x += 15

# Divide the x value by 5 using assignment operators
x = x / 5            # x /= 5

# Multiply the x value by 10 using assignment operator
x = x * 10       # x *= 10

# Get module of x on 3 using assignment operators
x = x % 3     # x %= 3

# Using python print the module of 11 to 4
print( 11 % 4 )

# Print the exponent of 2,3
print( 2 ** 3)

# Divide 11 by 3 using python division
11 / 3

# Can we divide 11 by 3 and get an integer number yes , we can
11 // 3 
# or 
c = 11 / 3
c = int (c)

# Check if 10 is bigger than 15 or not
print(10 > 15)

# If 10 is not bigger than15 print x is smaller than 15
if 10 < 15 :
    print("x is smaller than 15")

# If we need all the conditions to be true we will use …. or

# What is the differences between if , elif
# if is using in only one condition but elif there are more one condition

# What is the differences between elif else
# elif mean there are more one condition but else there is the last step or result 

# Can we use more than one elif yes

# Can we use more than one else NO

# write s simple ternary operator
s = 2
print("Even") if s % 2 == 0 else print("Odd")

# in elif , python will check all the conditions no matter what ?NO

# in elif we use else for ... ?
# last probabaly or result

# if we have this list [2,4,6,8,10] :
h = [2,4,6,8,10]

# check to see if 4 in this list or not
if 4 in h :
    print(True)
else:
    print(False)

# check to see if 4 and 6 in this list on not
if 4 and 6 in h :
    print(True)
else:
    print(False)

# check to see if 3 or 6 in this list
if 3 or 6 in h :
    print(True)
else:
    print(False)
    
# check to see if 2 , 4 and 5 in this list
if 2 and 4 and 5 in h :
    print(True)
else:
    print(False)














