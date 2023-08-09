import random
import time
computador = random.randint(0, 5)
print('+=+' * 18)
print('Tente advinha qual numero eu vou pensar entre 0 e 5.')
print('+=+' * 18)
jogador = int(input('Qual número estou pensando: '))
print('PENSANDO...')
time.sleep(2)

while computador != jogador:
    print('Você perdeu!')
    print('Tente novamente!')
    
    print('O número escolhido foi: {}'.format(computador))
    computador = random.randint(0, 5)
    print('+=+' * 18)
    print('Tente advinha qula numero eu vou pensar entre 0 e 5.')
    print('+=+' * 18)
    jogador = int(input('Qual número estou pensando: '))   
    print('PENSANDO...')
    time.sleep(2)
    
print('Você ganhou!')
print('O número escolhido foi: {}'.format(computador))

    