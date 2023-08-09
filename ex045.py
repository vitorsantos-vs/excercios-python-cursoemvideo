from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('=-' * 10)
print('Compuador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-' * 10)

if computador == 0: # computador jogou Pedra
    if jogador == 0: # jogador jogou pedra
        print('EMPATE')
    elif jogador == 1: # jogador jogou papel
        print('JOGADOR VENCE')
    elif jogador == 2: # jogador jogou tesoura
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 1: # computador jogou Papel
    if jogador == 0: # jogador jogou pedra
        print('COMPUTADOR VENCE')
    elif jogador == 1: # jogador jogou papel
        print('EMPATE')
    elif jogador == 2: # jogador jogou tesoura
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
        
elif computador == 2: # computador jogou Tesoura
    if jogador == 0: # jogador jogou pedra
        print('JOGADOR VENCE')
    elif jogador == 1: # jogador jogou papel
        print('COMPUTADOR VENCE')
    elif jogador == 2: # jogador jogou tesoura
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
        
