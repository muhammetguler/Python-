x = int(input())

sum = 0

if x < 0 and x > 9999:
    print('Input is not in the interval')
else:
    print(x//1000 + (x//100)%10 + (x//10)%10 + x%10)


