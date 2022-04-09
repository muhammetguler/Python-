x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    if y > z:
        print(z, x)
    else:
        print(y, x)

if y > x and y > z:
    if x > z:
        print(z, y)
    else:
        print(x, y)

if z > x and z > y:
    if x > y:
        print(y, z)
    else:
        print(x, z)

#Another Solution:

x = int(input())
y = int(input())
z = int(input())

min_number = z
max_number = z

if x > y and x > z:
    max_number = x
elif y > x and y > z:
    max_number = y

if x < y and x < z:
    min_number = x
if y < x and y < z:
    min_number = y

print(min_number, max_number)

'''
We can also calculate min and max with built-in functions:
- min = min(x,y,z)
- max = max(x,y,z)
'''