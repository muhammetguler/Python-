x = int(input())
y = int(input())

if x % y == 0:
    print('Divisible')
elif x % y != 0:
    print('Not divisible', x % y)