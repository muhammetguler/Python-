# Constants (Fixed values such as numbers, letters and strings)

print('Hi, Python')
print("Hello Python")
print(3)
print(5.6)

print('----------------')
# Variables (A variable is a memory location used to store a value)

x = 2
y = 2.3
z = 'k'
t = 'hello'

print(x)
print(x, y)

print('----------------')
#Statements

x = 5 #Assignment statement
x = x + 4 #Assignment with expression (The right side is an expression)
print(x) #Print Statement

print('----------------')
#Numeric Expressions

x = 44
y = 10
print(x + y)
print(x * y)
print(x % y)
print(y ** 2)

print('----------------')
#Order of Evaluation

x = 2 + 4 ** 3 / 4 * 6
print(x)

'''
Highest precedence rule to lowest precedence rule:
- Parentheses are always respected
- Exponentiation (raise to a power)
- Multiplication, Division, and Remainder
- Addition and Subtraction
- Left to righ
'''

print('----------------')
#Data Types

x = 'Hello'
y = 'Python'
z = x + y
print(x + ' ' + y)
print(z)
print(x,y)
print('Hello','Python')
print('Hello', 2022)

''' Notice: “+” means “addition” if something is a number 
and “concatenate” if something is a string '''

print('----------------')
#Type Matters

x = 'Hello'
y = 1.5
print(type(x))
print(type(y))
print(type(-5))

'''
Integers are whole numbers: -14, -2, 0, 1, 100, 401233
Floating Point Numbers have decimal parts: -2.5 , 0.0, 98.6, 14.0
'''

print('----------------')
#Type Conversions

x = 2
print(x, type(x))
x = float(x)
print(x, type(x))

print('----------------')
#Integer Division

print(8/4)
print(5/2)
print(4.0/4.0)
print(10/90)
print(5//2)

'''
Notice1: Integer division produces a 
floating point result
Notice2: If you want part after decimal 
point truncated you can use the 
// operator
'''

print('----------------')
#String Conversions

x = '12'
x = int(x)
print(x+1)

print('----------------')
#User Input

x = input()
print(x)
print(type(x))

y = 'Welcome'
z = input('What is your name? ')
print(y,z)
print(y+' '+ z)
print('Welcome',z)

'''
Notice: The input() function returns a string
'''

print('----------------')
#Coverting User Input

age = input('How old are you?')
age = int(age)
print(type(age))
print('Next year you will be', age+1, 'years old')