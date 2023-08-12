from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os número sorteado foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
    
print(f'\nO maior numero sorteado foi {max(numeros)}')
print(f'O menor numero sorteado foi {min(numeros)}')