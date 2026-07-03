# First program 

from os import name


print("Hello, World!")

print(23+3)
print(23-3)
print(23*3)
print(23/3)
print(23//3)
print(23%3)

# Variable is a container that holds data in memory.
x = 10
print(x)
c = 20
print(c)
name = "Jannat"
print("my name is", name)
print(type(name))
print(type(x))
print(type(c))
# Data types are the classification of data items. 
# It represents the kind of value that tells what operations can be performed on a particular data. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.
# Data types in Python are:
# 1. Numeric data type - Integer, Float, Complex
# 2. Text data type - String
# 3. Boolean data type - True, False
# 4. List data type - []
# 5. Tuple data type - ()
# 6. Dictionary data type - {}
name = 'Jannat'
name1 = "Jannat"
name2 = '''Jannat'''
jannat = 23
print (name)
print (name1)
print (name2)
print (jannat)
boolean1 = True
boolean2 = False
print (boolean1)
print (boolean2)
a =  None
age = 23
old = False 
a = None
print(type(old))
print (type(a))
# arthmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc. on numeric values.
a = 5
d = 2
print(a+d)
print(a-d)
print(a*d)
print(a/d)
print(a//d) #floor division(quotient)
print(a%d) #remainder
print(a**d) #exponential

# relational operators are used to compare two values. It returns either True or False according to the condition.
a = 5
d = 2
print(a>d) # True
print(a<d) # False
print(a==d) # False
print(a!=d) # True
print(a>=d) # True
print(a<=d) # False

# assignment operators are used to assign values to variables. It is a combination of arithmetic and assignment operator.
a = 5
a += 2  # equivalent to a = a + 2
print(a)  # 7
a -= 1  # equivalent to a = a - 1
print(a)  # 6
a *= 3  # equivalent to a = a * 3
print(a)  # 18
a /= 2  # equivalent to a = a / 2
print(a)  # 9.0
print(" a :", a)
num = 8
num **=8 
print ("num :", num)

# logical operators are used to combine conditional statements. It returns either True or False according to the condition.
a = 5
b = 4
print(a)
w = True
v = False
print( w and v )
print( not False)
print( not ( w < v ))
print ( w > v and w > 150 )
print ( "AND Operator :" , w and v )
print ( "OR Operator :" , w or v )
print ( "NOT Operator :", not v )
print ( "OR Operator :", a==b or a>b)

# Type conversion is the process of converting the data type of a value to another data type. It is also known as type casting. Python provides various built-in functions to perform type conversion.
# int() - converts a value to an integer data type.
# float() - converts a value to a floating-point data type.
# str() - converts a value to a string data type.   
a = 2
b = 4.35
sum =  a+b
print( " The sum of a and b is : ", sum)

# Type casting is the process of converting the data type of a value to another data type. It is also known as type conversion. Python provides various built-in functions to perform type casting.
# int() - converts a value to an integer data type. 
# float() - converts a value to a floating-point data type.
# str() - converts a value to a string data type.

a = int("234")
print(a)
# Example of type conversion
a = 2
b = 4.35
sum =  a+b
print( " The sum of a and b is : ", sum)

#   Example of type casting
a = int("234")      
print(a)

# Example of type conversion
a = 2
b = 4.35
sum =  a+b
print( " The sum of a and b is : ", sum)
#  Example of type casting
a = int("234")