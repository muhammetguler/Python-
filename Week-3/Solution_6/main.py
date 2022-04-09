x = int(input())
y = int(input())

if x>y:
    tmp = x
    x = y
    y = tmp

print(x,y)

''' 
Solution with Else:

if x>y:
    print(y,x)
else:
    print(x,y)
'''


a = int(input())
b = int(input())
c = int(input())


if a > b:
    tmp = a
    a = b
    b = tmp

if a > c:
    tmp = a
    a = c
    c = tmp

if b > c:
    tmp = b
    b = c
    c = tmp

print(a,b,c)


'''
Another solution:

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

middle = a + b + c - minimum - maximum
print(minimum, middle, maximum)

Notice: We can find middle in another way
if a != minimum and a != maximum:
    middle = a
if b != minimum and b != maximum:
    middle = b
if c != minimum and c != maximum:
    middle = c
'''

'''
Solution with Else:

if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)

if b>a and b>c:
    if a>c:
        print(c,a,b)
    else:
        (a,c,b)

if c>a and c>b:
    if b>a:
        print(a,b,c)
    else:
        print(b,a,c)
'''