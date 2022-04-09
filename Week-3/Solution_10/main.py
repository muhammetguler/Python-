temperature = int(input())

if temperature == 0:
    print('It can be solid or liquid.')
elif temperature == 100:
    print('It can be liquid or gas.')
elif temperature < 0:
    print('It is in the solid state. ')
elif temperature < 100:
    print('It is in the liquid state.')
else:
    print('It is in the gas state.')