x = float(input())
y = float(input())
z = float(input())

a = x // 1
b = y // 1
c = z // 1

print(x-a, y-b, z-c)
print("%.2f %.2f %.2f" % (x-a, y-b, z-c))

'''
Notice:
New:
"{0:.2f} {1:.3f}".format(12.3152, 89.65431)
Old:
"%.2f %.3f" % (12.3152, 89.65431)

Expected Output:
12.32 89.654
'''

