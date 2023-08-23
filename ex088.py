from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30) 
print(f'     SORTEIO MEGA SENA     ')
print('-' *30)
qtd_jogo = int(input('Quantos jogos você quer que eu sorteie? '))
total = 1
while total <= qtd_jogo:
    cont = 0
    while True:
        num = randint(1 , 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break        
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('=-' * 3, f'SORTEANDO {qtd_jogo} JOGOS ', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('=-' * 4, '< BOA SORTE! >', '=-' * 4)
