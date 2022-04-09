x = int(input())
y = int(input())
z = int(input())

if x <= 0 or y <=0 or z<=0:
    print('False')
elif x*x == y*y + z*z or y*y == x*x + z*z or z*z == x*x + y*y:
    print('True')

'''
You can use only one line of code to solve the problem.
print(not(x <= 0 or y <= 0 or z <= 0)and((x * x + y * y == z * z)or(x * x + z * z == y * y)or(y * y + z * z == x * x)))
'''