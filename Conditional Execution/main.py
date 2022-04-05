# Comparison Operators

x = 10

if x == 10:
    print('Equals 10')
if x > 9:
    print('Greater than 9')
if x >= 10:
    print('Greater than or Equals 10')
if x < 11:
    print('Less than 11')
if x <= 10:
    print('Less than or Equals 10')
if x != 11:
    print('Not equal 11')
print('Done!')

'''
Notice1: Increase indent after an if statement (after : )
Notice2: Maintain indent to indicate the scope of the block
Notice3: Reduce indent back to the level of the if statement to indicate the end of the block
Notice4: Blank lines are ignored - they do not affect indentation
Notice5: Comments on a line by themselves are ignored with regard to indentation
'''

print('----------------')
# Nested Decisions

x = 20
if x > 1:
    print('More than 1')
    if x < 40:
        print('Less than 40')
print('All done!')

print('----------------')
# Two-way Decisions with else

x = 5
if x > 4:
    print('Bigger')
else:
    print('Smaller')
print('All done!')

print('----------------')
# Multi-way

x = int(input())
if x < 10:
    print(x,'is smaller than 10')
elif x < 20:
    print(x, 'is smaller than 20')
else:
    print(x, 'is bigger than 10 and 20')
print('All done!')

print('----------------')
'''Exercise: Rewrite your pay computation to give the 
employee 1.5 times the hourly rate for hours 
worked above 40 hours.'''

pay = 0
hours = int(input())
if hours > 40:
    pay = 40 * 10 + (hours-40)*15
else:
    pay = hours * 10
print(pay)

print('----------------')
# Catching exceptions: The try / except structure

'''
Notice: You surround a dangerous section of code with try and 
except
•If the code in the try works - the except is skipped
•If the code in the try fails - it jumps to the except section
'''


str = input('Enter a number:')
try:
    num = int(str)
except:
    num = -1
if num > 0 :
    print('Good Job!')
else:
    print('Not a number!')


print('----------------')
'''Rewrite your pay program using try and except so that 
your program handles non-numeric input gracefully.'''

pay = 0
try:
    hours = int(input())
except:
    hours = -1
if hours > 40:
    pay = 40 * 10 + (hours-40)*15
    print(pay)
elif hours >= 0:
    pay = hours * 10
    print(pay)
else:
    print('Error, invalid input.')

'''
Notice: It works:
x = 2
x = 'Hello'
print(x)
'''

'''
Notice: cat is a Unix command that
shows the content of the
input file.
For example: $ cat pythonProject.py
'''