# while
num = int(input('Digite um numero para\ncalcular seu fatorial: '))
cont = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))

# for
'''
num = int(input('Digite um numero para\ncalcular seu fatorial: '))
cont = num
fat = 1
for i in range (num-1,-1,-1):
    print('{}'.format(i+1),end='')
    print(' X ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))
'''

# factorial
'''
from math import factorial
num = int(input('Digite um numero para\ncalcular seu fatorial: '))
f = factorial(num)
print('O fatoral de {} é {}.'.format(num, f))
'''