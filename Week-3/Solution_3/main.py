mass = int(input())
height_CM = int(input())
height_M = height_CM / 100

BMI = mass/(height_M**2)
print("{0:.1f}".format(BMI))

if BMI < 15:
    print('Very severely underweight')

elif BMI >= 15 and BMI < 16: # BMI < 16
    print('Severely underweight')

elif BMI >= 16 and BMI < 18.5: # BMI < 18.5
    print('Underweight')

elif BMI >= 18.5 and BMI < 25: # BMI < 25
    print('Normal (healthy weight)')

elif BMI >= 25 and BMI < 30: # BMI < 30
    print('Overweight')

elif BMI >= 30 and BMI < 35: # BMI < 35
    print('Obese Class I (Moderately obese)	')

elif BMI >= 35 and BMI < 40: # BMI < 40
    print('Obese Class II (Severely obese)	')
else:
    print('Obese Class III (Very severely obese)')