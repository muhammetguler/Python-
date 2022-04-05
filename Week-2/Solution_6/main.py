x = int(input())
y = int(input())
z = int(input())

sum = (x*(x%2) + y*(y%2) + z*(z%2))

print(sum)

print('--------------')
#Alternative Solution

x = int(input())
y = int(input())
z = int(input())

sum = 0

if x%2 != 0:
    sum = x
if y%2 != 0:
    sum = sum + y
if z%2 != 0:
    sum = sum + z

print(sum)